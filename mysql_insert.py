from mysql_util import MysqlUtil

db = MysqlUtil()
sql = """
INSERT INTO `category_temp` VALUES ('1', '女装男装');
"""

category = db.insert(sql)  # 获取多条记录

print("ok")