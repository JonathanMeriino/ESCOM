from flask import Flask, render_template, request,redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] ='Tobi.escom'
app.config['MYSQL_DB'] ='flask_password'
mysql= MySQL(app)

# settings

app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM contraseñas')
    data= cur.fetchall()
    return render_template('index.html',contraseñas = data)


@app.route('/add_contact',methods=['POST'])
def add_contact():
    if request.method == 'POST':
        social = request.form['social']
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        cur= mysql.connection.cursor()
        cur.execute('INSERT INTO contraseñas (redes_sociales, usuario, contraseñas) VALUES(%s, %s,%s)', 
        (social,usuario,contraseña))
        mysql.connection.commit()
        flash('Contraseña agregada exitosamente')
        return redirect(url_for('Index'))


@app.route('/edit')
def edit_contact():
    return 'edit_password'

@app.route('/delete')
def delete_contact():
    return 'delete_password'


if __name__ == '__main__':
    app.run(port = 3000, debug = True)