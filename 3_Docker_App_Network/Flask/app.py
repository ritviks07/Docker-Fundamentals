from flask import Flask
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask"

@app.route('/insert-data')
def insert_data():
    connection = pymysql.connect(
        host='mysql_container',
        user='root',
        password='demopassword',
        database='demodb'
    )

    cursor = connection.cursor()
    insert = "INSERT INTO USERS (city,temp) VALUES (%s, %s);"
    data = ("NYC",23)
    cursor.execute(insert,data)
    connection.commit()
    cursor.close()
    connection.close()

    return "Data inserted successfylly!"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)