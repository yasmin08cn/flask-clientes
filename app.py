from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('mysql.railway.internal', 'localhost')
app.config['MYSQL_USER'] = os.getenv('root', 'Yasmin')
app.config['MYSQL_PASSWORD'] = os.getenv('LNWbWmJZrXgEdJkJgzyemmbXzPqCYKzH', 'v5fVfeD9GelxC3s9')
app.config['MYSQL_DB'] = os.getenv('railway', 'meu_banco')


mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('add_cliente.html')

@app.route('/add', methods=['POST'])
def add_cliente():
    try:
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)', (nome, email, telefone))
        mysql.connection.commit()
        cursor.close()
        
        return "Cliente adicionado com sucesso!"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

if __name__ == '__main__':
    app.run(debug=True)
