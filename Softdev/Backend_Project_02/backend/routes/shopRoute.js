//Routing
const express = require('express')
const router = express.Router()
const { route } = require('express/lib/application')
const { timeout } = require('nodemon/lib/config')
const { update, db } = require('../models/shop')
const shop = require('../models/shop')
const shopPickup = require('../models/shopPickup')
const shopProduct = require('../models/shopProduct')
const productReview = require('../models/productReview')

// d.toLocaleString('en-US', { timeZone: 'America/New_York' })
// const asyncHandler = require('express-async-handler')
// //อ้างอิงตำแหน่งไฟล์
//const indexPage = path.join(__dirname,'../templates/index.html') 

//อัพโหลดไฟล์
const multer = require('multer')
const storage = multer.diskStorage({
    destination:function(req,file,cb){
        cb(null,'./backend/images/products') //ตำแหน่งจัดเก็บ
    },
    filename:function(req,file,cb){
        cb(null,Date.now()+'.jpg') //เปลี่ยนชื่อไฟล์ ป้องกันซ้ำ
    }
})
const upload = multer({
    storage:storage
})

//หน้าRegisterShop //ทำเทสในโพสแมนแล้ว
router.post('/api/register_shop/:userID', (req,res)=>{
    console.log(req.body.shopName)
    let data = new shop ({
        shopOwnerID: req.params.userID, 
        shopName: req.body.shopName, //error undefind งงๆ
        shopDescription: req.body.shopDescription,
        shopCategory: req.body.shopCategory,
        shopTel: req.body.shopTel
    })
    shop.registerShop(data,(err)=>{
        if(err) console.log(err)
    })
    // res.json("registerID")
    // res.redirect('/') //ไปซักหน้าอ่ะ
    res.status(200).json(data)
})

//หน้าเพิ่มเวลา pickup (อยู่หลังRegisterShop) //ทำเทสในโพสแมนแล้ว
router.post('/api/register_shopPickup/:shopID',(req,res)=>{
    let data = new shopPickup({
        shopID: req.params.shopID,
        pickupPlace: req.body.pickupPlace, //error ตรงนี้
        pickupTime: req.body.pickupTime 
    })
    shopPickup.registerShopPickup(data,(err)=>{
        if(err) console.log(err)
    })
    res.status(200).json(data)
    //res.redirect('/') //ไปซักหน้าอ่ะ
})

//เพิ่มสินค้า //เทสแล้ว //เหลืออัพรูป
router.post('/api/register_product/:shopID',upload.single('productPic'),(req,res)=>{
    console.log(req.file)
    let data = new shopProduct({
        shopID:req.params.shopID,
        productCategory:req.body.shopCategory,
        productName:req.body.productName,
        productPic:req.file.filename,
        productPrice:req.body.productPrice,
        productDescription:req.body.productDescription,
        productStock:req.body.productStock,
        productRating: 0,
        productSumOfRating: 0,
        productNumOfReview: 0
    })
    shopProduct.addProduct(data,(err)=>{
        if(err) console.log(err)
    })
    res.status(200).json(data)
    //res.redirect('/') //ไปซักหน้าอ่ะ
})

//เพิ่มReview //เทสแล้ว
router.post('/api/add_review/:productID/:shopID/:userID',(req,res)=>{
    const date = new Date().toLocaleString('en-US', { timeZone: 'Asia/Jakarta' });
    console.log(date); 
    let data = new productReview({
        productID:req.params.productID,
        shopID:req.params.shopID,
        reviewClientID:req.params.userID,
        reviewDescription:req.body.reviewDescription,
        reviewStar:req.body.reviewStar,
        reviewTime: date
    })
    let product1 = {
        $inc: {productNumOfReview: 1,productSumOfRating: req.body.reviewStar},
    }
    shopProduct.findByIdAndUpdate({_id : req.params.productID},product1,{useFindAndModify:false}).exec(err=>{
        shopProduct.find({_id : req.params.productID}).exec((err,doc)=>{
            const data = {shopProduct:doc}
            let product2 = {
                productRating: data.shopProduct[0].productSumOfRating/ data.shopProduct[0].productNumOfReview
            }
            console.log(product2)
            shopProduct.findByIdAndUpdate({_id : req.params.productID},product2,{useFindAndModify:false}).exec(err=>{
                if(err) console.log(err)
            })
        })
        productReview.addReview(data,(err)=>{
            if(err) console.log(err)
        })
        if(err) console.log(err)
    })
    
    res.status(200).json(data)
    //res.redirect('/') //ไปซักหน้าอ่ะ
})

//อัพเดตร้านค้า //เทสแล้ว
router.post('/api/update_shop/:shopID',(req,res)=>{
    let data = {
        shopOwnerID: req.body.userID, 
        shopName: req.body.shopName,
        shopDescription: req.body.shopDescription,
        shopTel: req.body.shopTel
    }
    shop.findByIdAndUpdate({_id: req.params.shopID},data,{useFindAndModify:false}).exec(err=>{
        if(err) console.log(err)
    })
    res.status(200).json(data)
    //res.redirect('/') //ไปซักหน้าอ่ะ
})

//อัพเดตpickup //เทสแล้ว
router.post('/api/update_shopPickup/:shopID',(req,res)=>{
    let data = ({
        pickupPlace: req.body.pickupPlace,
        pickupTime: req.body.pickupTime 
    })
    shopPickup.findOneAndUpdate({shopID: req.params.shopID},data,{useFindAndModify:false}).exec(err=>{
        if(err) console.log(err)
    })
    res.status(200).json(data)
})

//อัพเดตสินค้า //เทสแล้ว
router.post('/api/update_product/:productID',upload.single('productPic'),(req,res)=>{
    let data = ({
        productName:req.body.productName,
        productCategory:req.body.shopCategory,
        productPic:req.file.filename,
        productPrice:req.body.productPrice,
        productDescription:req.body.productDescription,
        productStock:req.body.productStock,
    })
    shopProduct.findOneAndUpdate({_id: req.params.productID},data,{useFindAndModify:false}).exec(err=>{
        if(err) console.log(err)
    })
    res.status(200).json(data)
    //res.redirect('/') //ไปซักหน้าอ่ะ
})

//ลบร้านค้าใช้ shopID //เทสแล้ว
router.post('/api/delete_shop/:shopID',(req,res)=>{ //หาด้วย shopID
    shop.findOneAndDelete({_id:req.params.shopID}).exec(err=>{
       if(err) console.log(err)
    })
    shopPickup.findOneAndDelete({shopID:req.params.shopID}).exec(err=>{
        if(err) console.log(err)
    })
    shopProduct.deleteMany({shopID:req.params.shopID}).exec(err=>{
        if(err) console.log(err)
    })
    productReview.deleteMany({shopID:req.params.shopID}).exec(err=>{
        if(err) console.log(err)
    })
    res.status(200).json('ok')
    //res.redirect('/') //ไปหน้าก่อนหน้า
})

//ลบร้านค้าใช้ userID //เทสแล้ว
router.post('/api/delete_shopByUser/:userID',(req,res)=>{ //หาด้วย shopID
    shop.find({shopOwnerID:req.params.userID}).exec((err,doc)=>{
        const data = {shop:doc}
        shopPickup.findOneAndDelete({shopID:data.shop[0]._id}).exec(err=>{
            if(err) console.log(err)
        })
        shopProduct.deleteMany({shopID:data.shop[0]._id}).exec(err=>{
            if(err) console.log(err)
        })
        productReview.deleteMany({shopID:data.shop[0]._id}).exec(err=>{
            if(err) console.log(err)
        })
        shop.findOneAndDelete({shopOwnerID:req.params.userID}).exec(err=>{
            if(err) console.log(err)
        })
    })
    res.status(200).json('ok')
    //res.redirect('/') //ไปหน้าก่อนหน้า
})

//ลบสินค้าใช้ productID //เทสแล้ว
router.post('/api/delete_product/:productID',(req,res)=>{
    shopProduct.findOneAndDelete({_id:req.params.productID}).exec(err=>{
        if(err) console.log(err)
    })
    console.log('deletepro')
    res.status(200).json('ok')
})

//ดึงข้อมูลร้านค้าที่มีอยู่ไปโชว์ ใช้ shopID //ใช้ได้ทั้งหน้าดู shop เฉยๆของเจ้าของลูกค้า และหน้าแก้ด้วย แต่ต้องแก้ redirect //เทสแล้ว
router.get('/api/show_infoShop/:shopID',(req,res)=>{ //หาด้วย shopID
    shop.find({_id : req.params.shopID}).exec((err,doc)=>{
        res.json({shop:doc}) //ส่งเป็น json
    })
    res.status(200)
    //res.redirect('/') //ไปหน้าก่อนหน้า
})

//ดึงข้อมูลร้านค้าที่มีอยู่ไปโชว์ ใช้ userID เจ้าของร้าน //เทสแล้ว
router.get('/api/show_infoShopByUser/:userID',(req,res)=>{ //หาด้วย shopID
    shop.find({shopOwnerID : req.params.userID}).exec((err,doc)=>{
        res.json({shop:doc}) //ส่งเป็น json
    })
    res.status(200)
    //res.redirect('/') //ไปหน้าก่อนหน้า
})

//ข้อมูล pickup ที่มีอยู่ไปโชว์ //ใช้ได้ทั้งหน้าลูกค้าเลือกเวลานัดรับ แม่ค้าแก้เวลานัดรับ //เทสแล้ว
router.get('/api/show_shopPickup/:shopID',(req,res)=>{ //หาด้วย shopID
    shopPickup.find({shopID : req.params.shopID}).exec((err,doc)=>{
        res.json({shopPickup:doc}) //ส่งเป็น json
    })
    res.status(200)
    //res.redirect('/') //ไปหน้าก่อนหน้า
})

//ดึงสินค้าในร้านค้านั้นๆไปแสดง //เทสแล้ว
router.get('/api/show_productByShop/:shopID',(req,res)=>{ //หาด้วย shopID
    shopProduct.find({shopID : req.params.shopID}).exec((err,doc)=>{
        res.json({shopProduct:doc}) //ส่งเป็น json
    })
    res.status(200)
    //res.redirect('/') //ไปหน้าก่อนหน้า
})

//ดึงสินค้าด้วยประเภท
router.get('/api/show_productByCategory/:productCategory',(req,res)=>{ //หาด้วย Category
    shopProduct.find({productCategory : req.params.productCategory}).exec((err,doc)=>{
        res.json({shopProduct:doc}) //ส่งเป็น json
    })
    res.status(200)
    //res.redirect('/') //ไปหน้าก่อนหน้า
})

//ดึงรีวิวของสินค้าชนิดนั้นๆไปแสดง //เทสแล้ว
router.get('/api/show_review/:productID',(req,res)=>{ //หาด้วย shopID
    productReview.find({productID : req.params.productID}).exec((err,doc)=>{
        res.json({productReview:doc}) //ส่งเป็น json
    })
    res.status(200)
    //res.redirect('/') //ไปหน้าก่อนหน้า
})

//แสดงสินค้าทั้งหมด //เทสแล้ว
router.get('/api/showAllProduct',(req,res)=>{
    shopProduct.find().exec((err,doc)=>{
        res.json({shopProduct:doc})
    })
    //res.redirect('/') //ไปหน้าก่อนหน้า
})

// router.get('/showProduct',(req,res)=>{ 
//     shop.find().exec((err,doc)=>{
//         res.json({product:doc})
//     })
// })

// router.get('/delete/:id',(req,res)=>{ //delete
//     shop.findByIdAndDelete(req.params.id,{useFindAndModify:false}).exec(err=>{
//         if(err) console.log(err)
//     })
// })

// router.post('/update',(req,res)=>{
//     const update_id = req.body.update_id
//     let data = {
//         name:req.body.name,
//         price:req.body.price,
//         description:req.body.description
//     }
//     shop.findByIdAndUpdate(update_id,data,{useFindAndModify:false}).exec(err=>{
//         if(err) console.log(err)
//     })
// })

module.exports = router