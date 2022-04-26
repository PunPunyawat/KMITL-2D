// ใช้งาน mongoose
const mongoose = require('mongoose')

// ออกแบบ Schema
let shopProductSchema = mongoose.Schema({
    shopID:String,
    productCategory:String,
    productName:String,
    productPic:String,
    productPrice:Number,
    productDescription:String,
    productStock:Number,
    productRating:Number,
    productSumOfRating:Number,
    productNumOfReview:Number
})

//สร้างโมเดล
let shopProduct = mongoose.model("shopProductInfo",shopProductSchema)

//ส่งออกโมเดล
module.exports = shopProduct

//ฟังก์ชั่นสำหรับบันทึกข้อมูล
module.exports.addProduct = function(model,data){
    model.save(data)
}

