const express =  require('express')
const router = express.Router()
const {getindex, setindex, updateindex, deleteindex} = require('../controllers/indexController')   //? import funcs in indexContro

const {protect} = require('../middleware/authenMiddleware')  //! ป้องกันโดยใช้ Authen


//? call funs in indexcontroller
// router.get('/',getindex)  
// router.post('/',setindex)
//* รวมเป็นก้อนเดียวได้โดย ถ้า path เหมือนกัน   มีการใช้ prtotect คือต้องใช้ token ถึงจะใช้เข้าถึงได้
router.route('/').get(protect,getindex).post(protect,setindex)
router.route('/:id').put(protect,updateindex).delete(protect,deleteindex)

module.exports = router  //* exports to another use it 