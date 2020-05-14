// From: https://www.npmjs.com/package/cors 

var express = require('express')
var cors = require('cors')
var app = express()
 
app.use(cors())
 
app.get('/products/:id', function (req, res, next) {
  res.json({msg: 'This is CORS-enabled for all origins!'})
})
 
var portNum = 8000
app.listen(portNum, function () {
  console.log('CORS-enabled web server listening on port ' + portNum)
})