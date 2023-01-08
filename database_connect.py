import mysql.connector as mc
mydb = mc.connect(
                host='localhost',
                user="root",
                password="",
                database="library"
            )
title = 'ashu'
id = 1
author = 'xyz'
publisher = 'abc'
mycursor = mydb.cursor()
query = "INSERT INTO book (id, title, author, publisher) VALUES (%s, %s, %s, %s)"
value = (id, title, author, publisher)
mycursor.execute(query, value)
mydb.commit()
