import mysql.connector



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
    except mysql.connector.Error:
        print("connection error")
except mysql.connector.Error:
    print("connection errors")

dbcursor.close()
mydb.close()

