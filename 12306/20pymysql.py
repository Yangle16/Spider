#-*- coding:utf-8 -*-
import pymysql.cursors

if __name__ == "__main__":
    conn = pymysql.connect(
        host = "localhost",
        port = 3306,
        user = 'root',
        password = '2008512lele',
        db = '12306_train',
        charset = 'utf8'
    )

    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO `train_info` VALUES ('G1006','深圳','武汉');"
            cursor.execute(sql)

        conn.commit()
        with conn.cursor() as cursor:
            # sql = "SELECT `train_code`, `start_staion`, `end_station` FROM train_info;"
            sql = "select * from shop_station limit 1000;"
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                print result[0], result[1], result[2], result[3], result[4], result[5], result[6]

    finally:
        conn.close()
