import sys
import pymysql

HOST = ""
PORT = 3306
USER = ""
PASS = "&"
DB = ""

def connect_bd():
    try:
        conn = pymysql.connect(
            host=HOST, port=PORT, user=USER, password=PASS, db=DB
        )
        return conn

    except Exception as e:
        print( "Ha ocurrido al intentarcon conectar" + DB)
        print(e)