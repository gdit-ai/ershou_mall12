

import pymysql
connectiont = pymysql.connect(
    host = 'localhost', # 主机名
    user = 'root',      # 数据库用户名
    password = '',  # 数据库密码
    db = 'new_shop',      # 数据库名
    charset = 'utf8',   # 字符集编码
    cursorclass = pymysql.cursors.DictCursor # 游标类型
)

# 数据列表
data = [("1",'Apple iPhone XS Max (A2103) 64GB 金色 全网通（移动4G优先版） 双卡双待','7299','/static/product_test/2.jpg'),
        ("2",'Apple 2019 MacBook Pro 16【带触控栏】九代六核i7 16G 512G深空灰','17333','/static/product_test/3.jpeg'),
        ]
cursor = connectiont.cursor() # 获取游标对象
try:
    # 执行sql语句，插入多条数据
    cursor.executemany("insert into product_temp(id, pname, old_price, images) values (%s,%s,%s,%s)", data)
    # 提交数据
    connectiont.commit()
except:
    # 发生错误时回滚
    print("发生错误时回滚")
    connectiont.rollback()

print("ok")
connectiont.commit()
cursor.close()      # 关闭游标
connectiont.close() # 关闭连接
