from flask import Flask,render_template
app = Flask(__name__)

from mysql_util import MysqlUtil


@app.route('/')
def index():

    db = MysqlUtil()
    sql = 'SELECT * FROM product'
    product_list = db.fetchall(sql)  # 获取多条记录
    print(product_list)

    return render_template("/test/table_c1.html", product_list= product_list)
app.run(debug=True)