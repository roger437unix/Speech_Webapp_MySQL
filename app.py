from flask import Flask, render_template
from flask_mysqldb import MySQL 

app = Flask(__name__)

app.config['MYSQL_USER'] = 'tux'
app.config['MYSQL_PASSWORD'] = 'Mud@r123'
app.config['MYSQL_HOST'] = ''
app.config['MYSQL_DB'] = 'db_azure'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM tbl_fala ORDER BY id DESC''')
    results = cur.fetchall()
       
    return render_template("index.html", len = len(results), results = results)        


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
