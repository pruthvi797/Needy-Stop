import mysql.connector
import requests

def check(user_username, user_password ):
      val = [user_username, user_password]
      print(val)
      mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sasaank7",
        database="needystop"
      )

      mycursor = mydb.cursor()
      sql1 = "SELECT CASE WHEN EXISTS (SELECT * FROM users WHERE username = '%s' AND password = '%s') THEN 'True' ELSE 'False' END;"
      Flag = mycursor.executemany(sql1, val)
      mydb.commit()
      if Flag == True:
          url = 'file:///C:/Users/Sasaank/Desktop/NeedyStop/index.html'
          x = requests.post(url)
      else:
          print("NO SUCH USER EXISTS")

