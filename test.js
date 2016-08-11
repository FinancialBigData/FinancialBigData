var express=require('express');
var app=express();


//连接数据库
var mysql = require('mysql');
var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database:'test'
});

connection.connect();
//查询
var selectSQL='select * from test';



var arr = [];

connection.query(selectSQL, function(err, rows) {
    if (err) throw err;
    for (var i = 0; i < rows.length; i++) {
        arr[i] = rows[i].name+" "+rows[i].number;
    }

    //把搜索值输出
    app.get('/', function(req, res) {
        res.send(arr);
    });



});


//关闭连接
connection.end();
app.listen(3000);