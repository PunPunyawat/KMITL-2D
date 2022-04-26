// ใช้งาน mongoose
const mongoose = require('mongoose')

// ออกแบบ Schema
let productReviewSchema = mongoose.Schema({
    productID:String,
    shopID:String,
    reviewClientID:String,
    reviewDescription:String,
    reviewStar:Number,
    reviewTime:String
})

//สร้างโมเดล
let productReview = mongoose.model("productReviewInfo",productReviewSchema)

//ส่งออกโมเดล
module.exports = productReview

//ฟังก์ชั่นสำหรับบันทึกข้อมูล
module.exports.addReview = function(model,data){
    model.save(data)
}
