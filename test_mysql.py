from mysql_util import MysqlUtil

#
# db = MysqlUtil()
#
# sql = 'SELECT * FROM product'
# product_list = db.fetchall(sql)  # 获取多条记录
#
# print(product_list)

# username = "bb"
# password = "123"
# email = "bb@qq.com"
# id = 123
# db = MysqlUtil()
# sql = "INSERT INTO user(id, username,password,email) \
# VALUES ('%s', '%s', '%s', '%s')" % (id, username, password, email)  # 插入数据的SQL语句
#
# product_list = db.insert(sql)  # 获取多条记录


db = MysqlUtil()
sql = 'SELECT * FROM product'
comment_products = db.fetchall(sql)  # 获取多条记录
print(comment_products)

