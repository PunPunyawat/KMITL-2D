const userModel = require('../models/userModel')
const jwt = require('jsonwebtoken') 
const bcrypt = require('bcryptjs')
const asyncHandle = require('express-async-handler')

// @desc       register new user
// @route      POST /api/user
// @access     Public
const registerUser = asyncHandle (async (req,res)=>{

    const {userID,userName,
        userSurename,userEmail,
        userPassword,userAddress,
        userProfilePic,userDescription,
        userInterest,userTel
    } = req.body

    if(!userID||!userName
        ||!userSurename||!userEmail
        ||!userPassword||!userAddress
        ||!userProfilePic||!userDescription
        ||!userInterest||!userTel){
            res.status(400)
            throw new Error("Please enter all data of USER !!")
        }

    
    //!  check user exists (เช็คว่ามี user นี้ไหม)
    const userExists = await userModel.findOne({userEmail})
    
    //! ถ้าเจอ user มีอยู่ 
    if(userExists){
        res.status(400)
        throw new Error('User already exists !!!!!')
    }

    //! Hash password (เข้ารหัสข้อมูล user)
    const salt =await bcrypt.genSalt(10) //* เข้ารหัส 10 ครั้ง
    const hashPassword = await bcrypt.hash(userPassword,salt) //* เข้ารหัสแล้ว

    //? create user 1 อัน ไปใส่ใน DB
    const registerUser = await userModel.create({
        userID: req.body.userID,
        userName: req.body.userName,
        userSurename: req.body.userSurename,
        userEmail: req.body.userEmail,
        userPassword: hashPassword,   //* hashed password (เข้ารหัสข้อมูล)
        userAddress: req.body.userAddress,
        userProfilePic: req.body.userProfilePic,
        userDescription: req.body.userDescription,
        userInterest: req.body.userInterest,
        userTel:req.body.userTel

    })

    if(registerUser){   //* เช็คชัวว่า registerUser ทำงานได้จริง ส่ง 201 คือ create success
        res.status(201).json({ 
            _id: registerUser.id,  //* ส่งข้อมูลกลับมาบางส่วนก็ได้
            userID: registerUser.userID,
            userEmail: registerUser.userEmail,
            token: generateToken(registerUser._id)   //? ให้ส่ง token กลับไปด้วย
        })
    }else{ 
        res.status(400)
        throw new Error("User Model is bad quality !")
    }

})






// @desc       Authenticate  user
// @route      POST /api/user/login
// @access     Public
const loginUser = asyncHandle (async(req,res)=>{
    const { userEmail, userPassword} = req.body

    //* check user email 
    const userlogin_email = await userModel.findOne({userEmail})

    // //*check email กับ pass ว่าตรงกันไหม โดยต้อง    (เอาค่าที่ใส่เข้ามา มาเทียบกับ , decode password) 
    if(userlogin_email && (await bcrypt.compare(userPassword,userlogin_email.userPassword))){
        res.json({
            _id: userlogin_email.id,  //* ส่งข้อมูลกลับมาบางส่วนก็ได้
            userID: userlogin_email.userID,
            userEmail: userlogin_email.userEmail,
            token: generateToken(userlogin_email._id) 
        })
    }else{
        res.status(400)
        throw new Error("Invalid hotmail and password")
    }

})






// @desc       Get  user data 
// @route      Get /api/user/me
// @access     Private
 //! หาโดยใช้ token ซึ่งไปทำงาน protect ก่อนแล้วส่ง req.user  มาเรียกใช้เรียกข้อมูลของ token นั้นได้
const getUser = asyncHandle (async(req,res)=>{       
    // const {_id,userID,userEmail} = await userModel.findById(req.user.id)
    // res.status(200).json({
    //     _id,
    //     userID,
    //     userEmail
    // })
    res.status(200).json(req.user)   //? ให้มันส่งกลับมาหมดเลย ยกเว้น userPassword ที่ไม่ select มาจาก protect
})






// @desc       update  user data 
// @route      PUT /api/user/editprofile/:id
// @access     Public
const updateUser = asyncHandle(async(req,res)=>{
    
    const {userName,userSurename,userAddress,
        userProfilePic,userDescription,userInterest} = req.body

    if(!userName||!userSurename||!userAddress
        ||!userProfilePic||!userDescription||!userInterest){
            res.status(400)
            throw new Error("Please enter all update data of USER !!")
        }


    const id_update = await userModel.findById(req.params.id)
    
    if(!id_update){
        res.status(400)
        throw new Error("not  found data user id in database !")
    }

    //!--------------- update ---------------------
    const updateall = ({
        userName: req.body.userName,
        userSurename: req.body.userSurename,
        userAddress: req.body.userAddress,
        userProfilePic: req.body.userProfilePic,
        userDescription: req.body.userDescription,
        userInterest: req.body.userInterest,
    })
    //!-----------------------------------------

    const update_userid = await userModel.findByIdAndUpdate(id_update,updateall,{new:true})
    res.status(200).json(update_userid)
})






// @desc       delete  user data 
// @route      DELETE /api/user/deleteme
// @access     Pravate
const deleteUser = asyncHandle (async(req,res)=>{
    const {userEmail,userPassword} = req.body   //? คือค่าท่าใส่มาใน postman ส่วนของ body

    const userDelete_confirmEmail = await userModel.findOne({userEmail})
    if(!userDelete_confirmEmail){
        res.status(400)
        throw new Error("Your Email is not found")
    }

    if(userDelete_confirmEmail && (await bcrypt.compare(userPassword,userDelete_confirmEmail.userPassword))){     
        await userDelete_confirmEmail.remove()
        res.status(200).json({deleteEmail : userDelete_confirmEmail.userEmail})
    }else{
        res.status(400)
        throw new Error("Password is wrong !!")

    }    
})






//* generate Token JWT
const generateToken = (id) =>{  //? รับ id มาแล้ว generate กับ process.env แล้วส่ง return กลับไป
    //* ต้องมีไอดีในการยืนยันตัว
    return jwt.sign({id},process.env.JWT_SECERT,{
        expiresIn: '30d'   //? เป็น option ให้มี expire ในเวลา 30 วัน
    })
}


module.exports = {
    registerUser,
    loginUser,
    getUser,
    updateUser,
    deleteUser,
}