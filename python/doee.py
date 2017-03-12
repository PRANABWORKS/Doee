import json
from flask import Flask, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__) #create app instance
app.config['MYSQL_DATABASE_USER'] = 'hackathon'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hackathon'
app.config['MYSQL_DATABASE_DB'] = 'doee'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('registerUser', methods=['POST'])
def register():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    username = request.form['username']
    password = request.form['password']
    
    sql = """
    INSERT INTO users
    VALUES('0','{}','{}','{}','{}')
    """.format(firstname,lastname,username,password)
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    
    return "Registration successful!"
    
@app.route('loginUser', methods=['POST'])
def loginUser():
    username = request.form['username']
    password = request.form['password']
    
    sql = """
    SELECT id,username,password,long,latt
    FROM user
    WHERE username='{}' AND password='{}'
    ;
    """.format(username,password)
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    
    if len(result) is 1:
        #constructing the dictionary for use for json
        out = {
        "userid":result[0][0],
        "firstname":result[0][1],
        "lastname":result[0][2],
        "username":result[0][3],
        }
        
        return json.dumps(out)
    else:
        return "Unsuccessful login!"
        
@app.route('/submitJob',methods['POST'])
def submitJob():
    category=request.form['category']
    date=request.form['date']
    employerid=request.form['employerid']
    
    #sql to get all the possible matches
    sql = """
    SELECT users.userid,users.firstname,users.lastname
    FROM users,userservices,services
    WHERE services.name='{}' AND services.serviceid=userservices.serviceid AND userservices.userid=users.userid AND users.isdoer is not '0';
    """.format(category)
    
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    
    #return a json dump of all possible matches
    somedict = {
        "firstname" : [x[0] for x in result]
        "lastname" : [x[1] for x in result]
        "userid" : [x[2] for x in result]
        "date" : date
        "employerid" : employerid
    }
    
    return jsin.dumps(somedict)

@app.route('/shutdown')
def shutdown():
    passkey=str(request.args.get('Passkey'))
    if passkey == "qwertz":
        shutdown_server()
        return 'Server shutting down...'
    else:
        return "You are not authorized to shut down the server!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',threaded=True)