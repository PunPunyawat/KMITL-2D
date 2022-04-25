const express = require('express')
const router = express.Router()
const {addProduct_tocart,delete_allCart,deleteProduct_tocart} = require('../controllers/cartController')
const {protect} = require('../middleware/authenMiddleware')


router.post('/user/cart-add',protect,addProduct_tocart);
router.delete('/delete-allcart',protect,delete_allCart);
router.put('/user/cart-delete',protect,deleteProduct_tocart)


module.exports = router
