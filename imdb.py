import sqlite3

def createTable():
        connection = sqlite3.connect("databases.db")

        connection.execute("INSERT INTO 'Kullanicilar' VALUES(?,?,?)",('ezel','k@gmail.com','ezel'))
        connection.commit()

        sonuc = connection.execute("SELECT * FROM Kullanicilar ")

        for data in sonuc:
            print ("Kullanici Adiniz: ",data[0])
            print ("Email : ",data[1])
            print ("Parola : ",data[2])

        connection.close()
createTable()


