const asyncHandler = require('express-async-handler')
const Order = require('../models/orderModel')

const createOrderByShopId = asyncHandler(async (req, res) => {
    const {
        orderClientID,
        orderTraderID,
        orderProduct,
        orderAddress,
        orderCancel,
        orderApprove,
        orderTrackNum,
        orderFinishClient,
        orderFinishTrader,
        orderFinish,
        orderPickup,
        orderPrice
    } = req.body
    const check_order_exist = await Order.findOne({orderTraderID, orderClientID})
    if(check_order_exist){
        res.status(400)
        throw new Error('This orderTraderID already exists')
    }
    const new_order = await Order.create({
        orderClientID: req.body.orderClientID,
        orderTraderID: req.body.orderTraderID,
        orderProduct: req.body.orderProduct,
        orderAddress: req.body.orderAddress,
        orderCancel: req.body.orderCancel,
        orderApprove: req.body.orderApprove,
        orderTrackNum: req.body.orderTrackNum,
        orderFinishClient: req.body.orderFinishClient,
        orderFinishTrader: req.body.orderFinishTrader,
        orderFinish: req.body.orderFinish,
        orderPickup: req.body.orderPickup,
        orderPrice: req.body.orderPrice
    })
    res.status(201).json({
        _id: new_order._id,
        orderClientID: new_order.orderClientID || "null",
        orderTraderID: new_order.orderTraderID || "null",
        orderProduct: new_order.orderProduct || "[]",
        orderAddress: new_order.orderAddress || "null",
    })
})

const getOrderByShopID = asyncHandler(async (req, res) =>{
    try{
        const order_by_shopID = await Order.find({orderTraderID: req.params.shopId})
        res.status(200).json(order_by_shopID)
    } catch(err){
        res.status(500).json(err)
    }
})

const getOrderByUserID = asyncHandler(async (req, res) =>{
    try{
        const order_by_userID = await Order.find({orderClientID: req.params.userId})
        console.log(order_by_userID)
        res.status(200).json(order_by_userID)
    } catch(err){
        res.status(500).json(err)
    }
})

const getAllOrder = asyncHandler(async (req, res) => {
    try{
        const orders = await Order.find()
        res.status(200).json(orders)
    } catch(err){
        res.status(500).json(err)
    }
})

module.exports = {
    createOrderByShopId,
    getAllOrder,
    getOrderByShopID,
    getOrderByUserID
}