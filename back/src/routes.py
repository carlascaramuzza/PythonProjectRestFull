from flask import Flask, request, jsonify

from config import config as dbConfig

from flask_mysqldb import MySQL

from app import app 

from models.entidades import Usuario, tipo_usuario, db

import jwt

from datetime import datetime, timedelta

from authentication import jwt_required


#app = Flask("Restaurante")

#conexao = MySQL(app)

# def username_validation(cpf):
#     cursor = conexao.connection.cursor()
#     sql = "SELECT cpf from usuario;"
#     cursor.execute(sql)
#     cpfs = cursor.fetchall()
#     for item in cpfs:
#         if item != cpf:
#             return 1
#         else: 
#             return None

def cpf_validacao(cpf):
    usuarios = Usuario.query.filter(Usuario.cpf==cpf).all()
    if len(usuarios) < 1:
        return 1
    else: 
        return None

# @app.route('/usuarios', methods=["GET"])
# def listar_usuarios():
#     try:
#         cursor = conexao.connection.cursor()
#         sql = "SELECT u.id, u.nome, u.username, u.genero, u.telefone, u.email, tu.nome as tipo_usuario  FROM usuario u INNER JOIN tipo_usuario tu ON tu.id = u.tipo_usuario_id;"
#         cursor.execute(sql)
#         dados = cursor.fetchall()
#         usuarios = []
#         for fila in dados:
#             usuario = {'id': fila[0],'nome': fila[1],'username': fila[2], 'genero': fila[3], 'telefone': fila[4], 'email': fila[5], 'tipo_usuario': fila[6]}
#             usuarios.append(usuario)
#         return jsonify({'usuarios': usuarios, 'mensagem': "Lista de Cursos"})
#     except Exception as ex:
#         return jsonify({'mensagem': "Error"})  

@app.route("/usuarios", methods=["GET"])
@jwt_required
def listar_usuarios(current_user):
    try:
        #usuarios = Usuario.query.join(tipo_usuario, Usuario.tipo_usuario_id == tipo_usuario.id).all()
        usuarios = Usuario.query.all()
        return jsonify([usuario.to_json() for usuario in usuarios])
    except Exception as ex:
        return jsonify({'mensagem': "Error"}) 

# @app.route('/usuarios/<id>', methods=['GET'])
# def listar_curso(id):
#     try:
#         cursor = conexao.connection.cursor()
#         sql = "SELECT u.id, u.nome, u.username, u.genero, u.telefone, u.email, tu.nome as tipo_usuario  FROM usuario u INNER JOIN tipo_usuario tu ON tu.id = u.tipo_usuario_id WHERE u.id = '{0}';".format(id)
#         cursor.execute(sql) 
#         dados = cursor.fetchone()
#         if dados != None:
#              usuario = {'id': dados[0],'nome': dados[1],'username': dados[2], 'genero': dados[3], 'telefone': dados[4], 'email': dados[5], 'tipo_usuario': dados[6]}
#              return jsonify({'usuarios': usuario, 'mensagem': "Usuario Encontrado!"})
#         else:
#              return jsonify({'mensagem': "Usuario não encontrado!"})    

#     except Exception as ex:
#         return jsonify({'mensagem': "Error"})


@app.route("/usuarios/<id>", methods=["GET"])
@jwt_required
def listar_usuario(current_user, id):
    if current_user.id == int(id) or current_user.tipo_usuario.nome == "administrador":
        try:
            usuario = Usuario.query.get(id)
            if usuario != None:
                return jsonify(usuario.to_json())
            else:
                return jsonify({'mensagem': "Usuario não encontrado!"})  
        except Exception as ex:
            return jsonify({'mensagem': "Error"}) 
    else:
        return jsonify({'mensagem': "Voce não tem permissão para ver dados de outros usuários!"}), 403


# @app.route('/login', methods=['POST'])
# def login():
#     try:
#         cursor = conexao.connection.cursor()
#         sql = """SELECT cpf, senha  FROM usuario 
#         WHERE cpf = '{0}' and senha = '{1}';""".format(request.json['cpf'],request.json['senha'])
#         cursor.execute(sql) 
#         dados = cursor.fetchone()
#         if dados != None:
#             #IMPLEMENTAR---------redirecionar para Home page
#             return jsonify({'mensagem': "LOGIN REALIZADO COM SUCESSO"})
#         else:
#             return jsonify({'mensagem': "FALHA NO LOGIN: Usuario não encontrado!"})    

#     except Exception as ex:
#         return jsonify({'mensagem': "Error"})

@app.route("/login", methods=["POST"])
def login():
    try:
        print(request.json['cpf'])
        usuario = Usuario.query.filter_by(cpf=request.json['cpf'], senha=request.json['senha']).first()       
        if usuario != None:
            payload = {
                "id": usuario.id,
                "exp": datetime.utcnow() + timedelta(minutes=30)
            }
            token = jwt.encode(payload, app.config['SECRET_KEY'])

            return jsonify({"token": token, 'mensagem': "LOGIN REALIZADO COM SUCESSO"})            
            #IMPLEMENTAR---------redirecionar para Home page          
        else:
            return jsonify({'mensagem': "FALHA NO LOGIN: Usuario não encontrado!"}) 
    except Exception as ex:
        return str(ex) 

# @app.route('/usuarios', methods=['POST'])   #não esquecer q no front tem q bloquear os campos senha e cpf com nros exato 10 e 11 e telefone 11
# def  inserir_usuario():
#     try:           
#             cursor = conexao.connection.cursor()
#             sql= """INSERT INTO usuario (nome, username, genero, cpf, telefone, email, senha, tipo_usuario_id) VALUES
#             ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}');""".format(request.json['nome'],request.json['username'],
#             request.json['genero'],request.json['cpf'],request.json['telefone'],request.json['email'],request.json['senha'],request.json['tipo_usuario_id'])
#             cursor.execute(sql)
#             validation = username_validation(request.json['cpf'])
#             if validation == 1:
#                 print('pasou')                
#                 conexao.connection.commit()
#                 print('pasou') 
#                 return jsonify({'mensagem': "CADSATRO REALIZADO COM SUCESSO"})
#             else: 
#                 return jsonify({'mensagem': "CPF JÁ EXISTENTE! POR FAVOR INSIRA OUTRO CPF."})
#     except Exception as ex:
#         return jsonify({'mensagem': "Error"})  

@app.route('/usuarios', methods=['POST'])   #não esquecer q no front tem q bloquear os campos senha e cpf com nros exato 10 e 11 e telefone 11
def  inserir_usuario():
    try:           
            print('pasou') 
            usuario = Usuario(nome=request.json['nome'],username=request.json['username'],genero=request.json['genero'],
            cpf=request.json['cpf'],telefone=request.json['telefone'],email=request.json['email'],senha=request.json['senha'], tipo_usuario_id=2)
            print('pasou') 
            validation = cpf_validacao(request.json['cpf'])
            print('pasouuuuuuuu') 
            if validation == 1:
                print(validation)      
                db.session.add(usuario)  
                db.session.commit()
                print('pasou commit') 
                return jsonify({'mensagem': "CADASTRO REALIZADO COM SUCESSO"})
            else: 
                return jsonify({'mensagem': "CPF JÁ EXISTENTE! POR FAVOR INSIRA OUTRO CPF."})
    except Exception as ex:
        return jsonify({'mensagem': "Error"})  


# @app.route("/pedidos", methods=["GET"])
# #@jwt_required
# def listar_pedidos():
#     try:
#         pedidos = Usuario.query.all()
#         return jsonify([pedido.to_json() for pedido in pedidos])
#     except Exception as ex:
#         return jsonify({'mensagem': "Error"})       
# 


@app.route('/pedidos', methods=['POST'])  
def  inserir_pedidos():
    try:           
            print('pasouuuu') 
            pedido = Pedido(data_pedido=request.json['data_pedido'],delivery=request.json['delivery'],valor_total=request.json['valor_total'],
            observacoes=request.json['observacoes'],status_pedido=request.json['status_pedido'],usuario=request.json['usuario'],endereco=request.json['endereco'])
            print('pasou') 
            if pedido != None:
                print(pedido)      
                db.session.add(pedido)  
                db.session.commit()
                print('pasou commit') 
                return jsonify({'mensagem': "PEDIDO REALIZADO COM SUCESSO"})
            else: 
                return jsonify({'mensagem': "ERRO NO PEDIDO"})
    except Exception as ex:
        return jsonify({'mensagem': "Error"})    

def pagina_nao_encontrada(error):
    return "<h1>Página buscada não existe</h1>"
   


#app.config.from_object(config['development'])   
app.register_error_handler(404, pagina_nao_encontrada)
app.run()