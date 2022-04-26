const cartModel = require('../models/cartModel')
// const bcrypt = require('bcryptjs')
const asyncHandle = require('express-async-handler')
const { db } = require('../models/cartModel')

//* เพิ่ม product cart
const addProduct_tocart = asyncHandle(async(req,res)=>{
                                         //! cart เหมือนค่าคงที่ ที่เราตั้งขึ้นแต่อันนี้เขียนสั้นกว่า
    cartModel.findOne({user:req.user._id}).exec((error,cart)=>{
        if(error) return res.status(400).json({error})

        //* กรณีเจอ id ที่เพิ่มมาแล้ว
        if(cart){
            //! if cart exists then update quality
            const cart_ProductID = req.body.cProductID  //! ตัวที่รับมาจาก body

            //?   หาตัวปัจจุบัน                                  //test00 ของ body ที่ใส่ใหม่ เช็คว่า test00 ตรงไหมกะอันเก่า
            const sameProductadd = cart.cartProduct.find(data => data.cProductID == cart_ProductID); 

            //! all price now
            // const calculate_allprice =  cart.cartallPrice
            

            //? id ตรงกัน
            if(sameProductadd){
                cartModel.findOneAndUpdate({"user":req.user._id, "cartProduct.cProductID" :cart_ProductID},{
                    // "$set":{
                    //     "cartProduct.$.cProductNum" : req.body.cProductNum
                    //     // "cartProduct" : {
                    //     //     ...req.body.cartProduct,
                    //     //     cProductNum : sameProductadd.cProductNum + req.body.cartProduct.cProductNum} 
                    //     // ,
                    //     // "cartallPrice" : req.body.cartProduct.cProductPrice + calculate_allprice,
                    // }
                    "$inc" : {"cartProduct.$.cProductNum": 1 ,"cartallPrice" : req.body.cProductPrice}       
                }).exec((error)=>{
                    if(error) return res.status(400).json({error})
                    // if(cart_sameProduct){
                    //     res.status(201).json({cart_sameProduct : "OK"})
                    // }
                })
            }
            else{
                cartModel.findOneAndUpdate({user:req.user.id},{
                    // "cartProduct" : req.body.cartProduct, //เพิ่มเงินได้
                    "$push":    { "cartProduct" :   
                                    {
                                        "cProductID" : req.body.cProductID,
                                        "cProductPrice": req.body.cProductPrice
                                    }
                                },   //! ไว้เพิ่ม object ตอน id(test000) ไม่เหมือน 
                     "$inc" : {"cartallPrice" : req.body.cProductPrice}
                }).exec((error)=>{
                    if(error) return res.status(400).json({error})
                    // if(cart_NewProduct){
                    //     return res.status(201).json({cart_NewProduct})
                    // }
                })
            }
            res.status(200).json({cart_NewProduct:'OK'})

        }
        else{  //! id cart not exists then create new cart
            const cart = new cartModel({
                user: req.user.id,
                cartID: req.body.cartID,
                cartProduct: [{"cProductID" : req.body.cProductID,"cProductPrice": req.body.cProductPrice}],
                cartallPrice: req.body.cProductPrice
            });
        
            cart.save((error,NewcartID)=>{
                if(error) return res.status(400).json({error})
                if(NewcartID){
                    return res.status(201).json({NewcartID})
                }
            });
        }
    })
    
})






//* delete all cart of 1 user
const delete_allCart = asyncHandle(async(req,res)=>{
    const data_delete = await cartModel.findOne({user:req.user._id})
    if(!data_delete){
        res.status(400)
        throw new Error("not found your id in cart")
    }
    await data_delete.remove()
    res.status(200).json({delete_data:data_delete})
})







//* ลด product cart
const deleteProduct_tocart = asyncHandle(async (req, res) => {
    //! cart เหมือนค่าคงที่ ที่เราตั้งขึ้นแต่อันนี้เขียนสั้นกว่า
    
    cartModel.findOne({user:req.user._id}).exec((error,_cart)=>{
        if (error) return res.status(400).json({error})
       
        if (_cart){
            //! if cart exists then update quality
            const cart_ProductID = req.body.cProductID  //! ตัวที่รับมาจาก body
            //?   หาตัวปัจจุบัน          
            const sameProductadd = _cart.cartProduct.find(data => data.cProductID == cart_ProductID);

            //? id ตรงกัน
            if (sameProductadd) {
                // console.log(sameProductadd.cProductNum);
                if(sameProductadd.cProductNum == 1){
                    console.log("pull in");
                    
                    cartModel.findOneAndUpdate({ "user": req.user._id,"cartProduct.cProductID" : cart_ProductID}, {
            
                    "$pull": { 
                        "cartProduct" : { 
                            cProductID: req.body.cProductID,
                            cProductNum : 1 , 
                            cProductPrice:req.body.cProductPrice}
                        },
                    "$inc" : {"cartallPrice" : -req.body.cProductPrice} 
                      
                    }).exec((error)=>{
                        if(error) return res.status(400).json({error})
                        console.log("--------- pull out OK -----------");
                    })      
                }

                else if(sameProductadd.cProductNum >= 2){
                    cartModel.findOneAndUpdate({ "user": req.user._id, "cartProduct.cProductID": cart_ProductID }, {
                        "$inc": { "cartProduct.$.cProductNum": -1, "cartallPrice": -req.body.cProductPrice }
                    }).exec((error) => {
                        if (error) return res.status(400).json({ error })
                    })
                }

                else{
                    return res.status(400).json({message:"Error because less 0"})
                }
            }

        }
                 
         res.status(200).json({ delete_product : 'OK' })    
    })

})





















// //* ลบ product cart
// const deleteProduct_tocart = asyncHandle(async (req, res) => {
//     //! cart เหมือนค่าคงที่ ที่เราตั้งขึ้นแต่อันนี้เขียนสั้นกว่า
//     cartModel.findOne({ user: req.user._id }).exec((error, cart) => {
//         if (error) return res.status(400).json({ error })

//         //* กรณีเจอ id 
//         if (cart) {
//             //! if cart exists then update quality
//             const cart_ProductID = req.body.cartProduct.cProductID  //! ตัวที่รับมาจาก body

//             //?   หาตัวปัจจุบัน                                  //test00 ของ body ที่ใส่ใหม่ เช็คว่า test00 ตรงไหมกะอันเก่า
//             const sameProductadd = cart.cartProduct.find(data => data.cProductID == cart_ProductID);

//             // //! all price now
//             // const calculate_allprice = cart.cartallPrice
          
//             //? id ตรงกัน
//             if (sameProductadd) {
//                 // console.log(sameProductadd.cProductNum);

//                 // if(sameProductadd.cProductNum===1){ 
//                 //     cartModel.findOneAndDelete({cartID: req.body.cartID}).exec(err=>{
//                 //         if(err) {console.log(err)}
//                 //     })
//                 //     res.status(200).json({message:"you delete product successfully"})
//                 // }
//                 // else{
//                 cartModel.findOneAndUpdate({ "user": req.user._id, "cartProduct.cProductID": cart_ProductID }, {
//                     // "$set": {
//                     //     "cartProduct": {
//                     //         ...req.body.cartProduct,
//                     //         cProductNum: sameProductadd.cProductNum - req.body.cartProduct.cProductNum
//                     //     }
//                     // },
//                     // "cartallPrice": calculate_allprice - req.body.cartProduct.cProductPrice
//                     "$inc" : {"cartProduct.$.cProductNum": -1 ,"cartallPrice" : -req.body.cProductPrice}     
//                 }).exec((error, delete_sameProduct) => {
//                     if (error) return res.status(400).json({ error })
//                     // if (delete_sameProduct) {
//                     //     return res.status(201).json({ delete_sameProduct })
//                     // }
//                 })
//             }
//         }


//             // //* ยังไม่ได้ใช้ 
//             // else {
//             //     cartModel.findOneAndUpdate({ user: req.user.id }, {
//             //         // "cartProduct" : req.body.cartProduct, //เพิ่มเงินได้
//             //         "$pop": { "cartProduct": req.body.cartProduct },   //! ไว้เพิ่ม object ตอน id(test000) ไม่เหมือน 
//             //         cartallPrice: req.body.cartProduct.cProductPrice - calculate_allprice
//             //     })
//             //         .exec((error, _cart) => {
//             //             if (error) return res.status(400).json({ error })
//             //             if (_cart) {
//             //                 return res.status(201).json({ _cart })
//             //             }
//             //         })
//             // }

//         // }

//         // else {  //! id cart not exists then create new cart
//         //     res.status(400)
//         //     throw new Error("on id in database")
//         // }
//     })

// })




module.exports = {
    addProduct_tocart,
    delete_allCart,
    deleteProduct_tocart,
}














//!------------------------------------- BACKUP
// const cartModel = require('../models/cartModel')
// // const bcrypt = require('bcryptjs')
// const asyncHandle = require('express-async-handler')


// const addProduct_tocart = asyncHandle(async(req,res)=>{
    
//     cartModel.findOne({user:req.user._id})
//     .exec((error,cart)=>{
//         if(error) return res.status(400).json({error})
//         if(cart){
//             //! if cart exists then update quality
//             const cart_ProductID = req.body.cartProduct.cProductID
//             const sameProductadd = cart.cartProduct.find(c => c.cProductID == cart_ProductID);

//             if(sameProductadd){
//                 cartModel.findOneAndUpdate({"user":req.user._id, "cartProduct.cProductID" :cart_ProductID},{
//                     "$set":{
//                         "cartProduct" : {
//                             ...req.body.cartProduct,
//                             cProductNum : sameProductadd.cProductNum + req.body.cartProduct.cProductNum
//                         }
//                     }
                    
//                     // "cartProduct" : {
//                     //         ...req.body.cartProduct,
//                     //         $inc:{"cProductNum" : 1
//                     //     }
//                     // }
//                 })
//                 .exec((error,_cart)=>{
//                     if(error) return res.status(400).json({error})
//                     if(_cart){
//                         return res.status(201).json({_cart})
//                     }
//                 })

//             }else{
//                 cartModel.findOneAndUpdate({user:req.user.id},{
//                     "$push":{
//                         "cartProduct" : req.body.cartProduct
//                     }
//                 })
//                 .exec((error,_cart)=>{
//                     if(error) return res.status(400).json({error})
//                     if(_cart){
//                         return res.status(201).json({_cart})
//                     }
//                 })
//             }

//         }else{  //! id cart not exists then create new cart
//             const cart = new cartModel({
//                 user: req.user.id,
//                 cartID: req.body.cartID,
//                 cartProduct: [req.body.cartProduct]
//             });
        
//             cart.save((error,cart)=>{
//                 if(error) return res.status(400).json({error})
//                 if(cart){
//                     return res.status(201).json({cart})
//                 }
//             });
//         }
//     })
    
// })




// //! delete all cart of 1 user
// const delete_allCart = asyncHandle(async(req,res)=>{
//     const data_delete = await cartModel.findOne({user:req.user._id})
//     if(!data_delete){
//         res.status(400)
//         throw new Error("not found your id in cart")
//     }
//     await data_delete.remove()
//     res.status(200).json({delete_data:data_delete})
// })





// module.exports = {
//     addProduct_tocart,
//     delete_allCart,
// }

