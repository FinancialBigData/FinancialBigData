var express=require('express');
var app=express();


//�������ݿ�
var mysql = require('mysql');
var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database:'test'
});

connection.connect();
//��ѯ
var selectSQL='select * from test';



var arr = [];

connection.query(selectSQL, function(err, rows) {
    if (err) throw err;
    for (var i = 0; i < rows.length; i++) {
        arr[i] = rows[i].name+" "+rows[i].number;
    }

    //������ֵ���
    app.get('/', function(req, res) {
        res.send(arr);
    });



});


//�ر�����
connection.end();
app.listen(3000);