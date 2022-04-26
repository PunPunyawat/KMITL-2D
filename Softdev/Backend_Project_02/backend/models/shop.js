// ใช้งาน mongoose
const mongoose = require('mongoose')

//เชื่อม mongodb
// mongoose.connect('mongodb+srv://admin101:admin101@cluster0.8fugg.mongodb.net/KMITLsquare?retryWrites=true&w=majority',{
//     useNewUrlParser:true,
//     useUnifiedTopology:true
// }).catch(err => console.log(err))

// mongoose.connect('mongodb://localhost:27017',{
//     useNewUrlParser:true,
//     useUnifiedTopology:true
// }).catch(err => console.log(err))

// ออกแบบ Schema
const shopSchema = mongoose.Schema({
    shopOwnerID:String,
    shopName:String,
    shopDescription:String,
    shopCategory:String,
    shopTel:String
})

//สร้างโมเดล
// module.exports  = mongoose.model("shopInfo",shopSchema)
let shop  = mongoose.model("shopInfo",shopSchema)

//ส่งออกโมเดล
 module.exports = shop

//ฟังก์ชั่นสำหรับบันทึกข้อมูล
module.exports.registerShop = function(model,data){
    model.save(data)
}

