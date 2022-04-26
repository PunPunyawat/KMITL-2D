// ใช้งาน mongoose
const mongoose = require('mongoose')

// ออกแบบ Schema
let shopPickupSchema = mongoose.Schema({
    shopID:String,
    pickupPlace: {
        type : [String]
    },
    pickupTime:{
        type: [String]
    } //หาตัวแปร time ไม่เจอ
})

//สร้างโมเดล
let shopPickup = mongoose.model("shopPickupInfo",shopPickupSchema)

//ส่งออกโมเดล
module.exports = shopPickup

//ฟังก์ชั่นสำหรับบันทึกข้อมูล
module.exports.registerShopPickup = function(model,data){
    model.save(data)
}
