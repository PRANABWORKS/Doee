import os
import json
from flask import Flask, request, session, g
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__) #create app instance
app.config['MYSQL_DATABASE_USER'] = 'hackathon'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hackathon'
app.config['MYSQL_DATABASE_DB'] = 'doee'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def hello():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM employer")
    data = cursor.fetchall()
    cursor.close()
    return json.dumps(data)
    
@app.route("/registerEmployer")
def registerEmployer():
    
    firstname = "default"
    lastname = "default"
    username = str(request.args.get('UserName'))
    password = str(request.args.get('Password'))
    email = "default"
    phonenumber = "123456789"
    address = "default"
    
    sql = "insert into employer values('0','"+firstname+"','"+lastname+"','"+username+"','"+password+"','"+email+"','"+phonenumber+"','"+address+"');"
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    
    return "Registration successful"

if __name__ == "__main__":
    app.run()