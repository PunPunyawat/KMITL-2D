const express = require('express')
const router = express.Router()
const {registerUser,loginUser,getUser,updateUser,deleteUser} = require('../controllers/userController')
const {protect} = require('../middleware/authenMiddleware')


router.post('/',registerUser)
router.post('/login',loginUser)
router.put('/editprofile/:id',updateUser)
router.get('/me',protect,getUser)   //! protect โดยต้องเข้าถึงโดย token ;ซึ่งทำงาน protect เสร็จแล้วค่อยไปทำ getUser
router.delete('/deleteme',deleteUser)

module.exports = router

