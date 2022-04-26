//* create functions

const asyncHandle = require("express-async-handler")  //? ตัวจัดการแทน tye catch
const indexModel = require('../models/indexModel')
const userModel = require('../models/userModel')




// @desc       GET index
// @route      GET /api/index
// @access     private
const getindex = asyncHandle(async (req,res)=>{        //! พา math id จาก token
    const indexdata_all = await indexModel.find({user : req.user.id})

    res.status(200).json(indexdata_all)
})





// @desc       SET index
// @route      POST /api/index
// @access     private
const setindex = asyncHandle( async (req,res)=>{
    if(!req.body.text){ 
        res.status(400)     //! คัดข้อมูลแค่แบบ text ถ้าไม่ใช่ ส่ง status 400 กลับไป
        throw new Error("WRONG pls add text ")   //! และบอกว่ามี ERROR ;throw เหมือน return คือจบการทำงานเลย และส่งไปใน errorMiddleware
    }   

    //! สร้างแล้วเอาข้อมูลลง DB 
    const postdata = await indexModel.create({
        text: req.body.text,
        name: req.body.name,
        user: req.user.id
    })

    res.status(200).json(postdata)
})





// @desc       PUT index
// @route      PUT /api/index/:id
// @access     private
const updateindex = asyncHandle( async (req,res)=>{
    const data_id = await indexModel.findById(req.params.id)

    if(!data_id){   //? กรณีไม่เจอ id
        res.status(400)
        throw new Error("indexdata not found")
    }

    //? ให้เข้าหาด้วย user id หรือ tokenนั่นเอง
    const user_token = await userModel.findById(req.user.id)
    if(!user_token){
        res.status(401)
        throw new Error("user not found")
    }

    //? make sure the logged in user match  data_id กับ user
    if(data_id.user.toString() !== user_token.id){
        res.status(401)
        throw new Error("user not authorized")
    }

    //? กรณีเจอ id                   //? เริ่ม อัพเดทข้อมูลลง DB     เลข id  , ข้อมูลที่จะ update , option
    const updatedata_id = await indexModel.findByIdAndUpdate(req.params.id,req.body,{new:true})

    res.status(200).json(updatedata_id)    //? ส่ง แบบ json
})







// @desc       DELETE index
// @route      DELETE /api/index/:id
// @access     private
const deleteindex =asyncHandle(async(req,res)=>{
    const data_id = await indexModel.findByIdAndRemove(req.params.id) //! id ที่รับมา

    if(!data_id){
        res.status(400)
        throw new Error("this id cant found !")
    }

     //? ให้เข้าหาด้วย user id หรือ tokenนั่นเอง
     const user_token = await userModel.findById(req.user.id) //! เอา token มาหา id

     if(!user_token){
         res.status(401)
         throw new Error("user not found")
     }
 
     //? make sure the logged in user match  data_id กับ user_token
     if(data_id.user.toString() !== user_token.id){
         res.status(401)
         throw new Error("user not authorized")
     }

    await data_id.remove()

    res.status(200).json({delete_id: req.params.id,delete_token_changeto_id: req.user.id})
})




module.exports = {
    getindex,
    setindex,
    updateindex,
    deleteindex
}