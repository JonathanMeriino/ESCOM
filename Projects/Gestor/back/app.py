from flask import Flask, render_template, request,redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ='passwords_db'
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


@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contraseñas WHERE id = %s',(id))
    data =cur.fetchall()
    return render_template('edit-password.html',usuario=data[0])


@app.route('/update/<id>',methods = ['POST'])

def update_contact(id):
    if request.method == 'POST':
        nombreSocial = request.form['social']
        nombreUser = request.form['usuario']
        nombrePass = request.form['contraseña']
        cur = mysql.connection.cursor()
        cur.execute(""" 
        UPDATE contraseñas
        SET redes_sociales = %s, 
            usuario = %s,
            contraseñas = %s
        WHERE id = %s    
        """,(nombreSocial,nombreUser,nombrePass,id))
        mysql.connection.commit()
        flash('Contraseña actualizada correctamente')    
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contraseñas WHERE id ={0}'.format(id))
    mysql.connection.commit()
    flash('Contraseña Borrada exitosamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)