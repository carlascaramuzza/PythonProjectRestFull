
from flask import Flask, request, jsonify

from sqlalchemy import delete

from config import config as dbConfig

from flask_mysqldb import MySQL

from app import app 

from models.entidades import item_pedido, Mesa, Pedido, Usuario, reserva_mesa, tipo_usuario, Produto, Endereco, db

import jwt

from datetime import datetime, timedelta

from authentication import jwt_required

#ENDERECO=======================================================================================
@app.route("/enderecos", methods=["GET"])
@jwt_required
def listar_enderecos(current_user):
    if current_user.tipo_usuario.nome == "administrador":
        try:
            enderecos = Endereco.query.all()
            return jsonify([endereco.to_json() for endereco in enderecos])
        except Exception as ex:
            return jsonify({'mensagem': "Error"}) 
    else:
        try:
            enderecos = Endereco.query.filter(current_user.id==Endereco.usuario_id)
            return jsonify([endereco.to_json() for endereco in enderecos])
        except Exception as ex:
            return jsonify({'mensagem': "Error"})


@app.route('/enderecos', methods=['POST'])  
@jwt_required
def  inserir_endereco(current_user):
    try:  
        endereco = Endereco(endereco=request.json['endereco'],bairro=request.json['bairro'],numero=request.json['numero'],
        usuario_id=current_user.id,cep=request.json['cep'],cidade=request.json['cidade'],estado=request.json['estado'])
        print(endereco)
        db.session.add(endereco)  
        db.session.commit()
        return jsonify({'mensagem': "ENDERECO CADASTARADO COM SUCESSO"})
       
    except Exception as ex:
        return jsonify({'mensagem': "Error"})   


@app.route("/enderecos/<id>", methods=["DELETE"])
@jwt_required
def deletar_endereco(id,current_user):   
    try:
        endereco = Endereco.query.get(id)
        if endereco != None:    
            if current_user.id == endereco.usuario_id:
                db.session.delete(endereco)  
                db.session.commit()
                return jsonify({'mensagem': "ENDERECO DELETADO COM SUCESSO!"})                  
            else:
                return jsonify({'mensagem': "SEM PERMISSÃO"}), 403   
        else:
            return jsonify({'mensagem': "ESTE ENDERECO NÃO EXISTE!"})  
    except Exception as ex:
        return jsonify({'mensagem': "Error"})    


@app.route("/enderecos/<id>", methods=["PUT"])
@jwt_required
def atualizar_endereco(id, current_user):   
    try:  
            enderecos = Endereco.query.get(id)  
            if current_user.id == enderecos.usuario_id:            
                endereco = request.json['endereco']
                bairro = request.json['bairro']
                cep = request.json['cep']
                numero = request.json['numero']
                estado = request.json['estado']
                cidade = request.json['cidade']                
                if endereco != None or bairro != None or cep != None or  numero != None or estado != None or cidade != None  :
                    enderecos.endereco =endereco
                    enderecos.bairro = bairro
                    enderecos.cep = cep
                    enderecos.numero = numero
                    enderecos.estado = estado
                    enderecos.cidade = cidade
                    db.session.commit()
                    return jsonify({'mensagem': "ENDERECO ALTERADO COM SUCESSO"})
                else: 
                    return jsonify({'mensagem': "ERRO NA ALTERAÇÃO DO ENDERECO!"})
            else:
                return jsonify({'mensagem': "SEM PERMISSÃO"}), 403          
    except Exception as ex:
        return str(ex)   


#USUARIOS=======================================================================================
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


@app.route("/usuarios/<id>", methods=["PUT"])
@jwt_required
def atualizar_usuario(id, current_user):   
    try:  
        usuario = Usuario.query.get(id)  
        if usuario != None:
            if current_user.id == usuario.id:            
                cpf = request.json['cpf']
                data_nascimento = request.json['data_nascimento']
                email = request.json['email']
                genero = request.json['genero']
                nome = request.json['nome']
                senha = request.json['senha']
                telefone = request.json['telefone']
                username = request.json['username']   
                if cpf != None or data_nascimento != None or email != None or  genero != None \
                    or nome != None or senha != None or telefone != None or username != None:
                    validation = cpf_validacao_current_user(cpf, id)
                    if validation == 1:
                        usuario.cpf = cpf                    
                        usuario.data_nascimento = data_nascimento
                        usuario.email = email
                        usuario.genero = genero
                        usuario.nome = nome
                        usuario.senha = senha
                        usuario.telefone = telefone
                        usuario.username = username
                        db.session.commit()
                        return jsonify({'mensagem': "USUARIO ALTERADO COM SUCESSO"})
                    else: 
                        return jsonify({'mensagem': "CPF JÁ EXISTENTE! POR FAVOR INSIRA OUTRO CPF."})    
                else: 
                    return jsonify({'mensagem': "ERRO NA ALTERAÇÃO DO USUARIO!"})
            else:
                return jsonify({'mensagem': "SEM PERMISSÃO"}), 403   
        else: 
            return jsonify({'mensagem': "USUARIO NÃO EXISTE!"})           
    except Exception as ex:
        return str(ex)   


@app.route("/usuarios/<id>", methods=["DELETE"])
@jwt_required
def deletar_usuario(id,current_user):
    if current_user.tipo_usuario.nome == "administrador":
        try:
            usuario = Usuario.query.get(id)
            if usuario != None:    
                db.session.delete(usuario)  
                db.session.commit()
                return jsonify({'mensagem': "USUARIO DELETADO COM SUCESSO!"})
            else:
                return jsonify({'mensagem': "ESTE USUARIO NÃO EXISTE!"})
        except Exception as ex:
            return jsonify({'mensagem': "Error"}) 
    else:
        return jsonify({'mensagem': "SEM PERMISSÃO"}), 403      

#LOGIN====================================================================================================
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


#PRODUTOS====================================================================================================        
@app.route("/produtos", methods=["GET"])
@jwt_required
def listar_produtos(current_user):    
        try:
            produtos = Produto.query.all()
            return jsonify([produto.to_json() for produto in produtos])
        except Exception as ex:
            return str(ex) 
# def listar_produtos():    
#         try:
#             produtos = Produto.query.all()
#             return jsonify([produto.to_json() for produto in produtos])
#         except Exception as ex:
#             return str(ex) 

@app.route("/produtos/<id>", methods=["PUT"])
@jwt_required
def atualizar_produtos(id, current_user):    
    if current_user.tipo_usuario.nome == "administrador":
        try:  
                produto = Produto.query.get(id)              
                nome = request.json['nome']
                preco = request.json['preco']
                categoria_id = request.json['categoria_id']
                if nome != None or preco != None or categoria_id != None:
                    produto.nome = nome
                    produto.preco = preco
                    produto.categoria_id = categoria_id
                    db.session.commit()
                    return jsonify({'mensagem': "PRODUTO ALTERADO COM SUCESSO"})
                else: 
                    return jsonify({'mensagem': "ERRO NA ALTERAÇÃO DO PRODUTO!"})
        except Exception as ex:
            return str(ex)   
    else:
        return jsonify({'mensagem': "SEM PERMISSÃO"}), 403  


@app.route("/produtos", methods=["POST"])
@jwt_required
def cadastrar_produto(current_user):
    if current_user.tipo_usuario.nome == "administrador":
        try:
            produto = Produto(nome=request.json['nome'], preco=request.json['preco'],categoria_id=request.json['categoria_id'])
            if produto != None:               
                db.session.add(produto)  
                db.session.commit()
                return jsonify({'mensagem': "CADASTRO DE PRODUTO REALIZADO COM SUCESSO"})
            else: 
                return jsonify({'mensagem': "ERRO NO PRODUTO"})
        except Exception as ex:
            return str(ex)  
    else:
        return jsonify({'mensagem': "SEM PERMISSÃO"}), 403  

@app.route("/produtos/<id>", methods=["DELETE"])
@jwt_required
def deletar_produto(id,current_user):
    if current_user.tipo_usuario.nome == "administrador":
        try:
            produto = Produto.query.get(id)
            if produto != None:    
                db.session.delete(produto)  
                db.session.commit()
                return jsonify({'mensagem': "PRODUTO DELETADO COM SUCESSO!"})
            else:
                return jsonify({'mensagem': "ESTE PRODUTO NÃO EXISTE!"})
        except Exception as ex:
            return jsonify({'mensagem': "Error"}) 
    else:
        return jsonify({'mensagem': "SEM PERMISSÃO"}), 403      
        


#PEDIDOS======================================================================================================
@app.route("/pedidos", methods=["GET"])
@jwt_required
def listar_pedidos(current_user):
    if current_user.tipo_usuario.nome == "administrador":
        try:
            pedidos = Pedido.query.all()
            print(pedidos)
            return jsonify([pedido.to_json_list() for pedido in pedidos])
        except Exception as ex:
            return jsonify({'mensagem': "Error"})  
    else:
        try:
            pedidos = Pedido.query.filter(Pedido.usuario_id==current_user.id).all()           
            return jsonify([pedido.to_json_list() for pedido in pedidos])
        except Exception as ex:
            return str(ex)    
# def listar_pedidos():  
#         try:
#             pedidos = Pedido.query.all()
#             teste = jsonify([pedido.to_json_list() for pedido in pedidos]) 
#             print(teste.json)
#             a = teste.json
#             print(type(a[0]['data_pedido']))
#             return teste
#         except Exception as ex:
#             return str(ex)    

@app.route("/itens_pedido/<pedido_id>", methods=["GET"])
@jwt_required
def listar_itens_pedido(pedido_id, current_user):    
        try:
            itens = item_pedido.query.filter(item_pedido.pedido_id == pedido_id).all()
            print(itens)
            return jsonify([item.to_json() for item in itens])
        except Exception as ex:
            return str(ex) 

@app.route('/pedidos', methods=['POST']) #LEMBRANDO QUE O VALOR TOTAL DO PEDIDO TEM Q SER CALCULADO NO FRONT PARA RECEBER NO BODY
@jwt_required 
def  inserir_pedidos(current_user):
    try:  
       
        pedido = Pedido(data_pedido=request.json['data_pedido'],delivery=request.json['delivery'],valor_total=request.json['valor_total'],
            observacoes=request.json['observacoes'],status_pedido_id=1,usuario_id=current_user.id,endereco_id=request.json['endereco_id'],
            itens=request.json['itens'])

        db.session.add(pedido) 
        db.session.commit()
        db.session.flush()

        itens = []
        for i in pedido.itens:  
            print('entrou')   
            print(i)   
            itens.append(item_pedido(pedido_id=pedido.id,produto_id=i['produto_id'],valor_unitario=i['valor_unitario'],
                qtd=i['qtd'],valor_total_itens=i['valor_total_itens']))

        if itens != None:
            for item in itens:
                db.session.add(item)
                db.session.commit()
        else: 
            return jsonify({'mensagem': "NÃO HÁ ITENS NO PEDIDO"})             

        return jsonify({'mensagem': "PEDIDO REALIZADO COM SUCESSO"})               

    except Exception as ex:
        return str(ex)    

@app.route('/pedidos/<id>', methods=['PUT']) 
@jwt_required 
def  alterar_status_pedido(id, current_user):
    if current_user.tipo_usuario.nome == "administrador":
        try:  
                pedido = Pedido.query.get(id)              
                status = request.json['status_pedido_id']
                if status != None:
                    pedido.status_pedido_id = status
                    db.session.commit()
                    return jsonify({'mensagem': "STATUS ALTERADO!"})
                else: 
                    return jsonify({'mensagem': "ERRO NO STATUS"})
        except Exception as ex:
            return str(ex)   
    else:
        return jsonify({'mensagem': "Sem permissão"}), 403                 

#MESAS================================================================================================
@app.route("/mesas", methods=["GET"])
@jwt_required
def listar_mesas(current_user):
    if current_user.tipo_usuario.nome == "administrador":
        try:
            mesas = Mesa.query.all()
            return jsonify([mesa.to_json_mesa() for mesa in mesas])
        except Exception as ex:
            return jsonify({'mensagem': "Error"}) 
    else:
        return jsonify({'mensagem': "Sem permissão"}), 403   

@app.route("/mesas", methods=["POST"])
@jwt_required
def cadastrar_mesa(current_user):
    if current_user.tipo_usuario.nome == "administrador":
        try:
            mesa = Mesa(numero=request.json['numero'], qtd_lugares=request.json['qtd_lugares'],area_interna=request.json['area_interna'])
            if mesa != None:               
                db.session.add(mesa)  
                db.session.commit()
                return jsonify({'mensagem': "CADASTRO DE MESA REALIZADO COM SUCESSO"})
            else: 
                return jsonify({'mensagem': "ERRO NO MESA"})
        except Exception as ex:
            return str(ex)  
    else:
        return jsonify({'mensagem': "Sem permissão"}), 403                

@app.route("/mesas/<id>", methods=["PUT"])
@jwt_required
def alterar_mesa(id,current_user):
    if current_user.tipo_usuario.nome == "administrador":
        try:
            mesa = Mesa.query.get(id)
            if mesa != None:
                qtd = request.json['qtd_lugares']
                area = request.json['area_interna']   
                if qtd != None or area != None:
                    mesa.qtd_lugares = qtd
                    mesa.area_interna = area
                    db.session.commit()
                    return jsonify({'mensagem': "MESA ALTERADA COM SUCESSO!"})
                else:
                    return jsonify({'mensagem': "NENHUMA ALTERAÇÃO REALIZADA"})    
            else:
                return jsonify({'mensagem': "ESTA MESA NÃO EXISTE!"})
        except Exception as ex:
            return jsonify({'mensagem': "Error"}) 
    else:
        return jsonify({'mensagem': "Sem permissão"}), 403           

@app.route("/mesas/<id>", methods=["DELETE"])
@jwt_required
def deletar_mesa(id,current_user):
    if current_user.tipo_usuario.nome == "administrador":
        try:
            mesa = Mesa.query.get(id)
            if mesa != None:    
                db.session.delete(mesa)  
                db.session.commit()
                return jsonify({'mensagem': "MESA DELETADA COM SUCESSO!"})
            else:
                return jsonify({'mensagem': "ESTA MESA NÃO EXISTE!"})
        except Exception as ex:
            return jsonify({'mensagem': "Error"}) 
    else:
        return jsonify({'mensagem': "Sem permissão"}), 403                  

#RESRVA DE MESAS=======================================================================================
@app.route("/reservamesas", methods=["GET"])
# @jwt_required
# def listar_reservamesas(current_user):
#     if current_user.tipo_usuario.nome == "administrador":
#         try:
#             reservas = reserva_mesa.query.all()
#             return jsonify([reserva.to_json_reserva() for reserva in reservas])
#         except Exception as ex:
#             return jsonify({'mensagem': "Error"}), 500
#     else:
#         try:
#             reservas = reserva_mesa.query.filter(reserva_mesa.usuario_id==current_user.id).all()
#             return jsonify([reserva.to_json_reserva() for reserva in reservas])
#         except Exception as ex:
#             return jsonify({'mensagem': "Error"}), 500
def listar_reservamesas():   
    try:
        reservas = reserva_mesa.query.all()
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

@app.route('/reservamesas/<id>', methods=['PUT']) 
@jwt_required
def  alterar_reserva_mesa(id, current_user):    
        try: 
            reserva = reserva_mesa.query.get(id)
            if current_user.id == reserva_mesa.usuario_id or current_user.tipo_usuario.nome == "administrador":
                mesa = request.json['mesa_id']
                data = request.json['data_reserva']
                if mesa != None or data != None:
                    validacao = validacao_reserva(data,mesa)
                    if validacao == 1:    
                        reserva.mesa_id = mesa
                        reserva.data_reserva = data
                        db.session.commit()
                        return jsonify({'mensagem': "RESERVA ALTERADA COM SUCESSO!"})
                    else:
                        return jsonify({'mensagem': "MESA JÁ RESERVADA!"})
                else:
                    return jsonify({'mensagem': "NENHUMA ALTERAÇÃO REALIZADA"})
            else:   
                 return jsonify({'mensagem': "Sem permissão"}), 403        

        except Exception as ex:
            return jsonify({'mensagem': "Error"})  

@app.route('/reservamesas/<id>', methods=['DELETE']) 
@jwt_required
def  delete_reserva_mesa(id, current_user):
    try: 
            reserva = reserva_mesa.query.get(id)
            if current_user.id == reserva_mesa.usuario_id or current_user.tipo_usuario.nome == "administrador":
                try: 
                    reserva = reserva_mesa.query.get(id)                    
                    if reserva != None:    
                        db.session.delete(reserva)  
                        db.session.commit()
                        return jsonify({'mensagem': "RESERVA DELETADA COM SUCESSO!"})
                    else:
                        return jsonify({'mensagem': "NÃO HÁ RESERVAS"})
                except Exception as ex:
                    return jsonify({'mensagem': "Error"})          
            else:   
                 return jsonify({'mensagem': "Sem permissão"}), 403 
    except Exception as ex:
        return jsonify({'mensagem': "Error"})  


#FUNÇÕES======================================================================================================
def validacao_reserva(data, mesa):
    reservas = reserva_mesa.query.filter(reserva_mesa.data_reserva==data, reserva_mesa.mesa_id==mesa).all()
    if len(reservas) < 1:
        return 1
    else: 
        return None

def cpf_validacao(cpf):
    usuarios = Usuario.query.filter(Usuario.cpf==cpf).all()
    if len(usuarios) < 1:
        return 1
    else: 
        return None

def cpf_validacao_current_user(cpf, id):   
    usuarios = Usuario.query.filter(Usuario.cpf==cpf).all()
    print(len(usuarios))
    if  len(usuarios) < 1 or (len(usuarios) == 1 and usuarios[0].id == int(id)) :
        return 1
    else: 
        return None        


def pagina_nao_encontrada(error):
    return "<h1>Página buscada não existe</h1>"  


#app.config.from_object(config['development'])   
app.register_error_handler(404, pagina_nao_encontrada)
app.run()