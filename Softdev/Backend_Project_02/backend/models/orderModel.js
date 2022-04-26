const mongoose = require('mongoose')
const orderSchema = mongoose.Schema({
    orderClientID: {
        type: String,
        //required: true
    },
    orderTraderID: {
        type: String,
        //required: true
    },
    orderProduct: [{
        oProductID: {
            type: String,
            //required: true
        },
        orderProductNum: {
            type: Number,
            //required: true
        },
        orderProductPrice: {
            type: Number,
            //required: true
        }
    }],
    orderAddress: {
        type: String,
    },
    orderCancel: {
        type: Boolean,
        //required: true
    },
    orderApprove: {
        type: Boolean,
        //required: true
    },
    orderTrackNum: {
        type: String
    },
    orderFinishClient: {
        type: Boolean,
        //required: true
    },
    orderFinishTrader: {
        type: Boolean,
        //required: true
    },
    orderFinish: {
        type: Boolean,
        //required: true
    },
    orderPickup: {
        oPickupPlace: {
            type: String
        },
        oPickupTime: {
            type: String
        }
    },
    orderPrice: {
        type: Number,
        default: 0
    }
},
{
    timestamps: true
})

module.exports = mongoose.model('Order', orderSchema)