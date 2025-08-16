import mysql.connector
from mysql.connector import Error


try:
    mydb = mysql.connector.connect(
        host = "",
        user = "",
        password = ""
    )

    dbcursor = mydb.cursor()

    dbcursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

    try:
        mydb = mysql.connector.connect(
            host = "",
            user = "",
            password = "",
            database = "alx_book_store"
        )
    except Error as e:
        print(e)
except Error as i:
    print(i)

dbcursor.close()
mydb.close()

