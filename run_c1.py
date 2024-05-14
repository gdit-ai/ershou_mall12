from flask import Flask, render_template,request,url_for,redirect,session
from mysql_util import MysqlUtil

app = Flask(__name__)
app.secret_key = 'mrsoft12345678' # 设置秘钥

@app.route('/')
def index():
    productList =[{'id': '0989b8f6d2a111e8a452b808cfd4f089', 'pname': 'Apple AirPods 蓝牙无线耳机 适用于iPhone7/8/X手机耳机',
      'images': 'http://qiniuyun.donghao.club/dd359563dc751ca5%20%281%29.jpg', 'counts': 1, 'old_price': 1299.0,
      'new_price': 1000.0}]
    productList1 = productList
    productList2 = productList
    productList3 = productList
    category = [
        {
            "id":1,
            "cname":"女装男装"
        },
        {
            "id": 2,
            "cname": "女装男装"
        },
        {
            "id": 3,
            "cname": "女装男装"
        },
        {
            "id": 4,
            "cname": "女装男装"
        },
    ]
    return render_template("/user/index.html", hot_products=productList, new_products=productList1,
                           extend_products=productList2, comment_products=productList3, categorys=category)

@app.route('/register', methods=['GET','POST'])
def register():

    if (request.method == "POST"):
        username = request.form['name']
        password = request.form['password']
        email = request.form['email']

        print(username)
        print(password)
        print(email)


        db = MysqlUtil()
        sql = "INSERT INTO user(username,password,email) \
        VALUES ('%s', '%s', '%s')" % (username,password,email) # 插入数据的SQL语句

        product_list = db.insert(sql)  # 获取多条记录

        print(product_list)

        # insert_data(username, password, email)
        # return render_template("index.html")
        return redirect(url_for('index'))

    else: #GET
         return render_template("/test/register.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if (request.method == "POST"):
        print("ok")
        username = request.form['username']
        password_candidate = request.form['password']
        print(username)
        sql = "SELECT * FROM user  WHERE username = '%s'" % (username)  # 根据用户名查找user表中记录
        db = MysqlUtil()  # 实例化数据库操作类
        result = db.fetchone(sql)  # 获取一条记录
        print(password_candidate)
        print(result)
        db_password = result['password']  # 用户填写的密码
        if password_candidate == db_password:
            # 写入session
            session['logged_in'] = True
            session['username'] = username

            # return "登录成功"# 跳转到控制台
            return redirect(url_for('index'))
        else:
            print("密码错误")
            return render_template("/test/login.html")

    else: #GET
         return render_template("/test/login.html")

@app.route('/logout')
def logout():
    session.clear() # 清除Session
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()