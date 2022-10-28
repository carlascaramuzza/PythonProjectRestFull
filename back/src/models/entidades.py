from enum import auto
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import JSON
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
    def to_json(self):
        return {
            'id': self.id,
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

class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    endereco = db.Column(db.String(255)) 
    bairro = db.Column(db.String(255))  
    numero = db.Column(db.Integer)  
    usuario_id = db.Column(db.Integer(), db.ForeignKey('usuario.id'))
    usuario = db.relationship("Usuario", backref="Endereco") 

    def to_json(self):
        return {
            'id': self.id,
            'endereco': self.endereco,
            'bairro': self.bairro,
            'numero': self.numero,           
            'usuario_id': self.usuario.id,
            'usuario': self.usuario.nome
        }    


class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data_pedido = db.Column(db.DateTime)
    delivery = db.Column(db.Integer)
    valor_total = db.Column(db.Float)
    observacoes = db.Column(db.String(50))
    status_pedido_id = db.Column(db.Integer(), db.ForeignKey('status_pedido.id'))
    status_pedido = db.relationship("Status_pedido", backref="Pedido")
    usuario_id = db.Column(db.Integer(), db.ForeignKey('usuario.id'))
    usuario = db.relationship("Usuario", backref="Pedido")
    endereco_id = db.Column(db.Integer(), db.ForeignKey('endereco.id'))
    endereco = db.relationship("Endereco", backref="Pedido")     
    itens = JSON
 
    def to_json(self):
        return {
            'id': self.id,
            'data_pedido': self.data_pedido,
            'delivery': self.delivery,
            'valor_total': self.valor_total,
            'observacoes': self.observacoes,
            'status_pedido_id': self.status_pedido.id,
            'status_pedido': self.status_pedido.status_pedido,
            'usuario_id': self.usuario.id,
            'usuario': self.usuario.nome,
            'endereco_id': self.endereco.id,
            'endereco': self.endereco.endereco,
            'itens': self.itens            
        } 
    def to_json_list(self):
        return {
            'id': self.id,
            'data_pedido': self.data_pedido,
            'delivery': self.delivery,
            'valor_total': self.valor_total,
            'observacoes': self.observacoes,
            'status_pedido_id': self.status_pedido.id,
            'status_pedido': self.status_pedido.status_pedido,
            'usuario_id': self.usuario.id,
            'usuario': self.usuario.nome,
            'endereco_id': self.endereco.id,
            'endereco': self.endereco.endereco
        }    
        

class Status_pedido(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    status_pedido = db.Column(db.String(50))


class item_pedido(db.Model):
    pedido_id = db.Column(db.Integer(), db.ForeignKey('pedido.id'), primary_key = True)
    pedido = db.relationship("Pedido", backref="item_pedido")
    produto_id = db.Column(db.Integer(), db.ForeignKey('produto.id'), primary_key = True)
    produto = db.relationship("Produto", backref="item_pedido")
    valor_unitario = db.Column(db.Float)
    qtd = db.Column(db.Integer)
    valor_total_itens = db.Column(db.Float)  

    def to_json(self):
        return {
            'pedido_id': self.pedido_id,
            'produto_id': self.produto_id,
            'produto': self.produto.nome,
            'valor_unitario': self.produto.preco,
            'qtd': self.qtd,
            'valor_total_itens' : self.valor_total_itens
        }
 
class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(255))
    preco = db.Column(db.Float)
    categoria_id =db.Column(db.Integer(), db.ForeignKey('categoria.id'))
    categoria = db.relationship("Categoria", backref="Produto")
    
    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'preco': self.preco,
            'categoria_id': self.categoria_id,
            'categoria': self.categoria.nome
        }



class Mesa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.Integer)
    qtd_lugares = db.Column(db.Integer)
    area_interna = db.Column(db.Integer)

    
    def to_json_mesa(self):
        return {
            'numero': self.numero,
            'qtd_lugares': self.qtd_lugares,
            'area_interna': self.area_interna
        }

class reserva_mesa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    mesa_id = db.Column(db.Integer, db.ForeignKey('mesa.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship("Usuario", backref="reserva_mesa")
    data_reserva = db.Column(db.Date)

    def to_json_reserva(self):
        return {
            'mesa_id': self.mesa_id,
            'usuario_id': self.usuario_id,
            'data_reserva': self.data_reserva,
            'usuario': self.usuario.nome
        }





    