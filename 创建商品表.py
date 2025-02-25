from mysql_util import MysqlUtil

db = MysqlUtil()
#导航表
sql = """
CREATE TABLE `user` (
  `id` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `addr` varchar(255) DEFAULT NULL,
  `is_ok` int(11) DEFAULT NULL,
  `img_url` text,
  `create_time` datetime DEFAULT NULL,
  `identity` int(11) DEFAULT NULL,
  `scores` int(11) DEFAULT NULL,
  `shop_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

category = db.insert(sql)  # 获取多条记录

# db = MysqlUtil()
# #导航表
# sql = """
# CREATE TABLE `category_temp` (
#   `id` varchar(50) NOT NULL,
#   `cname` varchar(255) NOT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
# """
#
# category = db.insert(sql)  # 获取多条记录

#商品表


db = MysqlUtil()

sql = """

CREATE TABLE `product_temp` (
  `id` varchar(50) NOT NULL,
  `pname` varchar(255) NOT NULL,
  `old_price` float NOT NULL,
  `new_price` float NOT NULL,
  `images` text,
  `is_hot` int(11) DEFAULT NULL,
  `is_sell` int(11) DEFAULT NULL,
  `pdate` datetime DEFAULT NULL,
  `click_count` int(11) DEFAULT NULL,
  `counts` int(11) NOT NULL,
  `uid` varchar(50) DEFAULT NULL,
  `pDesc` text,
  `love_user` text,
  `is_pass` int(11) DEFAULT NULL,
  `head_img` varchar(255) DEFAULT NULL,
  `csid` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

category = db.insert(sql)  # 获取多条记录
print("ok")