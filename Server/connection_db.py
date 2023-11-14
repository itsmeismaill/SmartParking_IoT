import pymysql


conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="smart_parking",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
