const mongoose = require('mongoose')

const userSchema = mongoose.Schema({
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
    
},{
    timestamps: true
})

module.exports = mongoose.model('USER',userSchema)