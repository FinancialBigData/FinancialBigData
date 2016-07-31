var express = require('express');
var router = express.Router();
var usr=require('dao/dbConnect');

/* GET home page. */
router.get('/', function(req, res) {
    if(req.cookies.islogin){
        req.session.islogin=req.cookies.islogin;
    }
if(req.session.islogin){
    res.locals.islogin=req.session.islogin;
}
  res.render('index', { title: '主页'});
});


router.route('/login')
    .get(function(req, res) {
        if(req.cookies.islogin){
            req.session.islogin=req.cookies.islogin;
        }
		if(req.session.islogin){
            res.locals.islogin=req.session.islogin;
        }
        res.render('login', { title: '用户登录'});
    })
    .post(function(req, res) {
        client=usr.connect();
        result=null;
        usr.selectFun(client,req.body.username, function (result) {
            if(result[0]===undefined){
                res.send('没有该用户');
            }else{
                if(result[0].PassWord===req.body.password){
                    req.session.islogin=req.body.username;
                    res.locals.islogin=req.session.islogin;
                    res.cookie('islogin',res.locals.islogin,{maxAge:60000});
                    res.redirect('/home');
                }else
                {
                    res.redirect('/login');
                }
               }
        });
    });

router.get('/logout', function(req, res) {
    res.clearCookie('islogin');
    req.session.destroy();
    res.redirect('/');
});

router.get('/home', function(req, res) {
	if(req.session.islogin){
        res.locals.islogin=req.session.islogin;
    }
	if(req.cookies.islogin){
        req.session.islogin=req.cookies.islogin;
    }
    res.render('home', { title: '用户中心', user: res.locals.islogin });
});

router.route('/reg')
    .get(function(req,res){
        res.render('reg',{title:'注册', user: res.locals.islogin});
    })
    .post(function(req,res) {
        client = usr.connect();
		result=null;
		usr.selectFun(client,req.body.username, function (result) {
            if(result[0]!==undefined)
			{
                res.send('用户已存在');
			}
			else{
			  usr.insertFun(client,req.body.username ,req.body.password2, function (err) {
              	if(err){ 
			  		throw err;
			  	}
			  	req.session.islogin=req.body.username;
              	res.locals.islogin=req.session.islogin;
              	res.cookie('islogin',res.locals.islogin,{maxAge:60000});
              	res.redirect('/home');
        		});	
			}
		})
    });

router.route('/buy')
	.get(function(req,res){
		if(req.session.islogin){
        res.locals.islogin=req.session.islogin;
    }
	if(req.cookies.islogin){
        req.session.islogin=req.cookies.islogin;
    }
    res.render('buy', { title: '购买股票', user: res.locals.islogin });
		})
	.post(function(req,res){
		})
		
router.route('/appoint')
	.get(function(req,res){
		if(req.session.islogin){
        res.locals.islogin=req.session.islogin;
    }
	if(req.cookies.islogin){
        req.session.islogin=req.cookies.islogin;
    }
    res.render('appoint', { title: '市价委托', user: res.locals.islogin });
		})
	.post(function(req,res){
		})
		
router.route('/own')
	.get(function(req,res){
		if(req.cookies.islogin){
        req.session.islogin=req.cookies.islogin;
    }
		if(req.session.islogin){
        res.locals.islogin=req.session.islogin;
		client = usr.connect();
		result=null;
		usr.selectHad(client,req.session.islogin, function (result) {
			if(result[0]!==undefined)
			{res.locals.had=result;
			}
		result=null;
		usr.selectOrder(client,req.session.islogin,function(result){
			if(result[0]!==undefined)
			{res.locals.order=result;
			}
			res.render('own',{ title: '我的股票'});
		});
		});
	    }
		})
	.post(function(req,res){
		})
		
router.route('/search')
	.get(function(req,res){
		if(req.session.islogin){
        res.locals.islogin=req.session.islogin;
    }
	if(req.cookies.islogin){
        req.session.islogin=req.cookies.islogin;
    }
    res.render('search', { title: '查询'});
		})
	.post(function(req,res){
		})



module.exports = router;
