from enum import auto
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app

#app = Flask(__name__)
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer(), primary_key = True, autoincrement=True)
    username = db.Column(db.String(20))
    nome = db.Column(db.String(50))
    genero = db.Column(db.String(1))
    cpf = db.Column(db.String(11))
    telefone = db.Column(db.Integer())
    email = db.Column(db.String(50))
    senha = db.Column(db.String(50))    
    tipo_usuario_id = db.Column(db.Integer(), db.ForeignKey('tipo_usuario.id'))
    tipo_usuario = db.relationship("tipo_usuario", backref="Usuario")
    #pedidoId = db.Column(db.Integer(), db.ForeignKey('pedido.id'))# aquia   a mesma coisa dos outros tabela 1 : * 1 não recebe fk da muitos

    def to_json(self):
        return {
            #'id': self.id,
            'nome': self.nome,
            'username': self.username,
            'genero': self.genero,
            'cpf': self.cpf,
            'telefone': self.telefone,
            'email': self.email,
            'senha' : self.senha,
            'tipo_usuario' : self.tipo_usuario.nome
        }

class tipo_usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100)) 
    #usuarioId = db.Column(db.Integer, db.ForeignKey('usuario.id'))# aquia   a mesma coisa dos outros tabela 1 : * 1 não recebe fk da muitos
    

# class Pedido(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     data_pedido = db.Column(db.DateTime)
#     delivery = db.Column(db.Integer)
#     valor_total = db.Column(db.Float)
#     observacoes = db.Column(db.String(50))
#     status_pedido_id = db.Column(db.Integer(), db.ForeignKey('status_pedido.id'))
#     status_pedido = db.relationship("status_pedido", backref="Pedido")
#     usuario_id = db.Column(db.Integer(), db.ForeignKey('usuario.id'))
#     usuario = db.relationship("usuario", backref="Pedido")
#     endereco_id = db.Column(db.Integer(), db.ForeignKey('endereco.id'))
#     endereco = db.relationship("endereco", backref="Pedido")        
#    # statusPedido = db.relationship('StatusPedido', backref = 'pedido')
#     #itemPedido = db.Column(db.Integer, db.ForeignKey('itemPedido.id')) #porque foi criado esse ?? o relacionamento é 1:* é a tabela de item q recebe o id..pq pode ter mais de 1 item

#     def to_json(self):
#         return {
#             #'id': self.id,
#             'data_pedido': self.nome,
#             'delivery': self.username,
#             'valor_total': self.genero,
#             'observacoes': self.cpf,
#             'status_pedido': self.status_pedido.status_pedido,
#             'usuario': self.usuario.nome,
#             'endereco': self.endereco.endereco
            
#         }    

class StatusPedido(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    statusPedido = db.Column(db.String(50))
   # pedidoId = db.Column(db.Integer(), db.ForeignKey('pedido.id'))# mesma coisa eh data 1:* a tabela 1 não recebe o Id de muitos.. é uam taberla de apoio

class ItemPedido(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    #pedidoId = db.relationship('Pedido', backref = 'itemPedido')
    #produtoId = db.relationship('Produto', backref = 'itemPedido')
    valorUnitario = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    valorTotal = db.Column(db.Float)

 
#CATEGORIA


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(255))
    preco = db.Column(db.Float)
    categoria = db.Column(db.String(255))
    #itemPedido = db.Column(db.Integer, db.ForeignKey('itemPedido.id')) #a mesma coisa aqui????



#MESA

#RESERVA MESA





    