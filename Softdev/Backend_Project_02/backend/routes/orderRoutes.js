const express = require('express')
const router = express.Router()
const {
    createOrderByShopId,
    getAllOrder,
    getOrderByShopID,
    getOrderByUserID
} = require('../controllers/orderController')


router.route('/').post(createOrderByShopId).get(getAllOrder)
router.route('/shopId/:shopId').get(getOrderByShopID)
router.route('/userId/:userId').get(getOrderByUserID)
module.exports = router