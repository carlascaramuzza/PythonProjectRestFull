from flask import Flask, request, jsonify

from config import config as dbConfig

from flask_mysqldb import MySQL

from app import app 

from models.entidades import Mesa, Pedido, Usuario, reserva_mesa, tipo_usuario, db

import jwt

from datetime import datetime, timedelta

from authentication import jwt_required

def cpf_validacao(cpf):
    usuarios = Usuario.query.filter(Usuario.cpf==cpf).all()
    if len(usuarios) < 1:
        return 1
    else: 
        return None

#GET - USUARIOS===================
@app.route("/usuarios", methods=["GET"])
@jwt_required
def listar_usuarios(current_user):
    if current_user.tipo_usuario.nome == "administrador":
        try:
            usuarios = Usuario.query.all()
            return jsonify([usuario.to_json() for usuario in usuarios])
        except Exception as ex:
            return jsonify({'mensagem': "Error"}) 
    else:
        try:
            usuarios = Usuario.query.filter(current_user.id==Usuario.id)
            return jsonify([usuario.to_json() for usuario in usuarios])
        except Exception as ex:
            return jsonify({'mensagem': "Error"}) 



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

@app.route('/usuarios', methods=['POST'])   #não esquecer q no front tem q bloquear os campos senha e cpf com nros exato 10 e 11 e telefone 11
def  inserir_usuario():
    try:           
            
            usuario = Usuario(nome=request.json['nome'],username=request.json['username'],genero=request.json['genero'],
            cpf=request.json['cpf'],telefone=request.json['telefone'],email=request.json['email'],senha=request.json['senha'], tipo_usuario_id=2)
            
            validation = cpf_validacao(request.json['cpf'])
            if validation == 1:
                print(validation)      
                db.session.add(usuario)  
                db.session.commit()
                return jsonify({'mensagem': "CADASTRO REALIZADO COM SUCESSO"})
            else: 
                return jsonify({'mensagem': "CPF JÁ EXISTENTE! POR FAVOR INSIRA OUTRO CPF."})
    except Exception as ex:
        return jsonify({'mensagem': "Error"})  


@app.route("/pedidos", methods=["GET"])
@jwt_required
def listar_pedidos(current_user):
    if current_user.tipo_usuario.nome == "administrador":
        try:
            pedidos = Pedido.query.all()
            return jsonify([pedido.to_json() for pedido in pedidos])
        except Exception as ex:
            return jsonify({'mensagem': "Error"})  
    else:
        try:
            pedidos = Pedido.query.filter(Pedido.usuario_id==current_user.id).all()           
            return jsonify([pedido.to_json() for pedido in pedidos])
        except Exception as ex:
            return str(ex)  




@app.route('/pedidos', methods=['POST']) 
@jwt_required 
def  inserir_pedidos(current_user):
    try:  
            pedido = Pedido(data_pedido=request.json['data_pedido'],delivery=request.json['delivery'],valor_total=request.json['valor_total'],
            observacoes=request.json['observacoes'],status_pedido_id=request.json['status_pedido_id'],usuario_id=current_user.id,endereco_id=request.json['endereco_id'])
           
            if pedido != None:
                print(pedido)      
                db.session.add(pedido)  
                db.session.commit()
                print('pasou commit') 
                return jsonify({'mensagem': "PEDIDO REALIZADO COM SUCESSO"})
            else: 
                return jsonify({'mensagem': "ERRO NO PEDIDO"})
    except Exception as ex:
        return str(ex)    


@app.route("/mesas", methods=["GET"])
#@jwt_required
def listar_mesas():
    try:
        mesas = Mesa.query.all()
        return jsonify([mesa.to_json_mesa() for mesa in mesas])
    except Exception as ex:
        return jsonify({'mensagem': "Error"}) 


@app.route("/reservamesas", methods=["GET"])
@jwt_required
def listar_reservamesas(current_user):
    if current_user.tipo_usuario.nome == "administrador":
        try:
            reservas = reserva_mesa.query.all()
            return jsonify([reserva.to_json_reserva() for reserva in reservas])
        except Exception as ex:
            return jsonify({'mensagem': "Error"}), 500
    else:
        try:
            reservas = reserva_mesa.query.filter(reserva_mesa.usuario_id==current_user.id).all()
            return jsonify([reserva.to_json_reserva() for reserva in reservas])
        except Exception as ex:
            return jsonify({'mensagem': "Error"}), 500


@app.route('/reservamesas', methods=['POST']) 
@jwt_required
def  reservar_mesa(current_user):
    try: 
        reserva = reserva_mesa(mesa_id=request.json['mesa_id'],usuario_id=current_user.id,data_reserva=request.json['data_reserva'])
        validacao = validacao_reserva(reserva.data_reserva,reserva.mesa_id)
        if validacao == 1:    
            db.session.add(reserva)  
            db.session.commit()
            return jsonify({'mensagem': "RESERVA REALIZADA COM SUCESSO!"})
        else:
            return jsonify({'mensagem': "MESA JÁ RESERVADA!"})
           
    except Exception as ex:
        return jsonify({'mensagem': "Error"})  

def validacao_reserva(data, mesa):
    reservas = reserva_mesa.query.filter(reserva_mesa.data_reserva==data, reserva_mesa.mesa_id==mesa).all()
    if len(reservas) < 1:
        return 1
    else: 
        return None


def pagina_nao_encontrada(error):
    return "<h1>Página buscada não existe</h1>"
   


#app.config.from_object(config['development'])   
app.register_error_handler(404, pagina_nao_encontrada)
app.run()