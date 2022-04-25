//* จักการเกี่ยวกับ Error 

const errorHandler = (err,req,res,next)=>{
    const statusCode = res.statusCode ? res.statusCode : 500  //? ดู statuscoded
    res.status(statusCode)

    res.json({  
        message : err.message,  //? ข้อความจาก error ในส่วน throw new Error
        stack : process.env.NODE_ENV === 'product' ? null : err.stack   
    })
}


module.exports = {
    errorHandler
}