from flask import Flask,render_template,request
import MySQLdb as mysql

con = mysql.connect(user='web',passwd='web',host='localhost',db='r')

con.autocommit(True)
cur = con.cursor()
app = Flask(__name__)
import json

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    sql = 'select * from memory'
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():
        arr.append([i[1]*1000,i[0]])
    return json.dumps(arr)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
