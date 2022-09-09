from flask import Flask, request, jsonify

from config import config

from flask_mysqldb import MySQL

app = Flask("Restaurante")

conexao = MySQL(app)

@app.route('/usuarios', methods=["GET"])
def listar_usuarios():
    try:
        cursor = conexao.connection.cursor()
        sql = "SELECT u.id, u.nome, u.username, u.genero, u.telefone, u.email, tu.nome as tipo_usuario  FROM usuario u INNER JOIN tipo_usuario tu ON tu.id = u.tipo_usuario_id;"
        cursor.execute(sql)
        dados = cursor.fetchall()
        usuarios = []
        for fila in dados:
            usuario = {'id': fila[0],'nome': fila[1],'username': fila[2], 'genero': fila[3], 'telefone': fila[4], 'email': fila[5], 'tipo_usuario': fila[6]}
            usuarios.append(usuario)
        return jsonify({'usuarios': usuarios, 'mensagem': "Lista de Cursos"})
    except Exception as ex:
        return jsonify({'mensagem': "Error"})  

@app.route('/usuarios/<id>', methods=['GET'])
def listar_curso(id):
    try:
        cursor = conexao.connection.cursor()
        sql = "SELECT u.id, u.nome, u.username, u.genero, u.telefone, u.email, tu.nome as tipo_usuario  FROM usuario u INNER JOIN tipo_usuario tu ON tu.id = u.tipo_usuario_id WHERE u.id = '{0}';".format(id)
        cursor.execute(sql) 
        dados = cursor.fetchone()
        if dados != None:
             usuario = {'id': dados[0],'nome': dados[1],'username': dados[2], 'genero': dados[3], 'telefone': dados[4], 'email': dados[5], 'tipo_usuario': dados[6]}
             return jsonify({'usuarios': usuario, 'mensagem': "Usuario Encontrado!"})
        else:
             return jsonify({'mensagem': "Usuario não encontrado!"})    

    except Exception as ex:
        return jsonify({'mensagem': "Error"})


def pagina_nao_encontrada(error):
    return "<h1>Página buscada não existe</h1>"
   


app.config.from_object(config['development'])   
app.register_error_handler(404, pagina_nao_encontrada)
app.run()