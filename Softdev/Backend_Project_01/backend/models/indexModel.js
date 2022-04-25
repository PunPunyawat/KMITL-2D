const mongoose = require('mongoose')


//? create schema
const indexSchema = mongoose.Schema(
    {
        user: {
            type: mongoose.Schema.Types.ObjectId,
            required: true,
            ref:'User'
        },
        text: {
            type: String,
            username : String,
            required : [true," YES PLS"],
        },
        name: {type:String},
    },
    {
        timestamps: true,
    }
)
                    //? ชื่อโมเดล(collection) , มีการจัดเก็บโครงสร้าง 
module.exports = mongoose.model('userindex',indexSchema)