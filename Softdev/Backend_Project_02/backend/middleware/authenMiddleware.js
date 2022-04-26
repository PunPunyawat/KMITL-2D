const jwt = require('jsonwebtoken')
const asyncHandle = require('express-async-handler')
const userModel = require('../models/userModel')

const protect = asyncHandle(async(req,res,next)=>{
    let token
 
    //? check authen ที่เป็น token ซึงต้องส่ง token ไป
    if(req.headers.authorization && req.headers.authorization.startsWith('Bearer')){   //* เช็คว่ามี token ไหม
        try {    //* get token from header(authen ที่ใส่ Bearer token)
            token = req.headers.authorization.split(' ')[1]  //? เอาค่า token ออกมาโดยมันมีช่องว่าง 1 เลยใส่ 1

            //! verify token decode (decode กลับมา โดยใช้ JWT_SECERT ในการคิดด้วย)
            const decoded = jwt.verify(token,process.env.JWT_SECERT)
            
            //* get user from the token      (select เลือกเอาค่าที่ต้องกการ แต่กรณีนี้ ไม่เอา userPassword ที่เหลือเอาหมดแล้วส่งกลับไปให้ที่ฟังชั่นที่เรียกใช้ protect โดยค่าต่างๆจะเก็บในคำว่า req.user )
            req.user = await userModel.findById(decoded.id).select('-userPassword')

            next()
        } catch (error) {
            console.log(error);
            res.status(401)
            throw new Error('Not Autherized')
        }
    }

    if(!token){    //* ไม่มี token ส่งมา
        res.status(401)
        throw new Error('Not Autherized, No Token')

    }
}) 

module.exports = { protect}