import mysql.connector as sql

try:
    db=sql.connect(host="localhost",port=3306,user="root",password="root",database="wd_12")
    cur=db.cursor()
    cur.execute("select * from banking")
    
except Exception:
    print("DataBase is not available")

else:
    print("true")
