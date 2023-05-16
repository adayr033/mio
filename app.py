from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

@app.route('/')
def Indexx():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()

    return render_template('indexx.html',   students=data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO  students (nombre, email, telefono) VALUES (%s, %s, %s)", (nombre, email, telefono))
        mysql.connection.commit()
        return redirect(url_for('Indexx'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM  students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Indexx'))



@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']

        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE  students SET nombre=%s, email=%s, telefono=%s
        WHERE id=%s
        """, (nombre, email, telefono, id_data))
        flash("Data Updated Successfully")
        return redirect(url_for('Indexx'))




if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='4000')