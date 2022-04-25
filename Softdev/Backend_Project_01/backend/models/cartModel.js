const mongoose = require('mongoose')

const cartSchema = mongoose.Schema({
    user: {
        type: mongoose.Schema.Types.ObjectId,
        required: true,
        ref:'User'
    },
    cartID:{
        type: String,
        required: true
    },
    cartProduct:[
        {
            cProductID: {   //! ต้องเอา _id product มาใช้
                // type: mongoose.Schema.Types.ObjectId,
                type: String,
                required : true,
                // ref:'Shop'

            },
            cProductNum:{
                type: Number,
                default: 1,
            },
            cProductPrice: {
                type: Number,
                required:true
            }
        }
    ],
    cartallPrice:{
        type: Number,
        // required:true,
        default: 0
    },

},{
    timestamps: true
})

module.exports = mongoose.model('Cart',cartSchema)