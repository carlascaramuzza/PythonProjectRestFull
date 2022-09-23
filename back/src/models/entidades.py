from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    genero = db.Column(db.String(1))
    cpf = db.Column(db.String(11))
    telefone = db.Column(db.Integer(15))
    email = db.Column(db.String(50))
    senha = db.Column(db.String(50))
    tipoUsuario = db.relationship('TipoUsuario', backref = 'usuario')
    pedidoId = db.Column(db.Integer, db.ForeignKey('pedido.id'))

class TipoUsuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    usuarioId = db.Column(db.Integer, db.ForeignKey('usuario.id'))

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.relationship('Usuario', backref = 'pedido')
    dataPedido = db.Column(db.DateTime)
    delivery = db.Column(db.Integer)
    valorTotal = db.Column(db.Float)
    endereco = db.Column(db.String(150))
    observacoes = db.Column(db.String(50))
    statusPedido = db.relationship('StatusPedido', backref = 'pedido')
    itemPedido = db.Column(db.Integer, db.ForeignKey('itemPedido.id'))

class StatusPedido(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    statusPedido = db.Column(db.String(50))
    pedidoId = db.Column(db.integer, db.ForeignKey('pedido.id'))

class ItemPedido(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pedidoId = db.relationship('Pedido', backref = 'itemPedido')
    produtoId = db.relationship('Produto', backref = 'itemPedido')
    valorUnitario = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    valorTotal = db.Column(db.Float)
    
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(255))
    preco = db.Column(db.Float)
    categoria = db.Column(db.String(255))
    itemPedido = db.Column(db.Integer, db.ForeignKey('itemPedido.id'))





    