const express = require('express')
const dotenv = require('dotenv').config()
const port = process.env.PORT || 3300
const colors =require('colors')
const {errorHandler} = require('./middleware/errorMIddleware')
const connectDB = require('./config/db')
const router = require('./routes/shopRoute')

connectDB()
const app = express()
app.use(express.json())
app.use(express.urlencoded({extended:false}))


app.use('/api/index',require('./routes/indexRoute'))
app.use('/api/user',require('./routes/userRoute'))
app.use('/api/cart',require('./routes/cartRoute'))
app.use('/api/orders', require('./routes/orderRoutes'))
app.use(router)

app.use(errorHandler)  //? จัดการ error

app.listen(port,()=> console.log(`Server Start Successfully on port ${port} !!`))