const mongoose = require('mongoose')

const userSchema = mongoose.Schema({
    userID:{
        type: String,
        required: [true,' Please enter your id !!'],
        unique: true
    },
    userName:{
        type: String,
        required: [true,' Please enter your name !!']
    },
    userSurename:{
        type: String,
        required: [true,' Please enter your surename !!']
    },
    userEmail:{
        type: String,
        required: [true,' Please enter your email !!'],
        unique: true
    },
    userPassword:{
        type: String,
        required: [true,' Please enter your password !!']
    },
    userAddress:{
        type: String,
        required: [true,' Please enter your address !!']
    },
    userProfilePic:{
        type: String,
        required: [true,' Please enter your profilepic !!']
    },
    userDescription:{
        type: String,
        required: [true,' Please enter your description !!']
    },
    userInterest:{
        type: String,
        required: [true,' Please enter your interest !!']
    },
    userTel:{
        type: String,
        required: [true,' Please enter your tel !!'],
        unique: true
    },
    

    //! เดี๋ยวลองดูอีกที คิดว่าอาจจะทำแยก func กัน
    // userShopFollwed:{
    //     type: String,
    //     required: [True,' Please enter your shopfoll !!']
    // },
    
    // userCart:{
    //     type: String,
    //     required: [True,' Please enter your cart !!']
    // },
    
    
},{
    timestamps: true
})

module.exports = mongoose.model('USER',userSchema)