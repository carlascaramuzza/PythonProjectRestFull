from flask_sqlalchemy import SQLAlchemy
from app import app

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

class Endereco(db.Model):
    id = db.Column(db.Integer(), primary_key = True, autoincrement=True)
    endereco = db.Column(db.String(255))
    bairro = db.Column(db.String(255))
    numero = db.Column(db.Integer())
    usuario_id = db.Column(db.Integer(), db.ForeignKey('usuario.id'))
    usuario = db.relationship("usuario", backref="Endereco")

    def to_json(self):
        return {
            'id': self.id,
            'endereco': self.endereco,
            'bairro': self.bairro,
            'numero': self.numero,
            'usuario': self.usuario.nome
        }

class tipo_usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100)) 
    #usuarioId = db.Column(db.Integer, db.ForeignKey('usuario.id'))# aquia   a mesma coisa dos outros tabela 1 : * 1 não recebe fk da muitos

    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome
        }
    

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    usuario_id = db.Column(db.Integer(), db.ForeignKey('usuario.id'))
    usuario = db.relationship('usuario', backref = 'Pedido')
    data_pedido = db.Column(db.DateTime)
    delivery = db.Column(db.Integer)
    valor_total = db.Column(db.Float)
    endereco_id = db.Column(db.Integer(), db.ForeignKey('endereco.id'))
    endereco = db.relationship('endereco', backref = 'Endereco')
    observacoes = db.Column(db.String(50))
    status_pedido_id = db.Column(db.Integer(), db.ForeignKey('status_pedido.id'))
    status_pedido = db.relationship('status_pedido', backref = 'StatusPedido')
   # statusPedido = db.relationship('StatusPedido', backref = 'pedido')
    #itemPedido = db.Column(db.Integer, db.ForeignKey('itemPedido.id')) #porque foi criado esse ?? o relacionamento é 1:* é a tabela de item q recebe o id..pq pode ter mais de 1 item

    def to_json(self):
        return {
            'id': self.id,
            'usuario': self.usuario.nome,
            'data_pedido': self.data_pedido,
            'delivery': self.delivery,
            'valor_total': self.valor_total,
            'endereco': self.endereco,
            'observacoes': self.observacoes,
            'status_pedido': self.status_pedido.status_pedido
        }

class StatusPedido(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    status_pedido = db.Column(db.String(50))
   # pedidoId = db.Column(db.Integer(), db.ForeignKey('pedido.id'))# mesma coisa eh data 1:* a tabela 1 não recebe o Id de muitos.. é uam taberla de apoio

class ReservaMesa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    mesa_id = db.Column(db.Integer(), db.ForeignKey('mesa.id'))
    mesa = db.relationship('mesa', backref = 'Mesa')
    usuairo_id = db.Column(db.Integer(), db.ForeignKey('usuario.id'))
    usuario = db.relationship('usuario', backref = 'Usuario')
    data_reserva = db.Column(db.DateTime)

    def to_json(self):
        return {
            'id': self.id,
            'mesa': self.mesa.numero,
            'usuario': self.usuario.nome,
            'data_reserva': self.data_reserva
        }

class Mesa(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.Integer())
    qtd_lugares = db.Column(db.Integer)
    area_interna = db.Column(db.Integer)


class ItemPedido(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pedido_id = db.Column(db.Integer(), db.ForeignKey('pedido.id'))
    pedido = db.relationship('pedido', backref = 'Pedido')
    produto_id = db.Column(db.Integer(), db.ForeignKey('produto.id'))
    produto = db.relationship('produto', backref = 'Produto')
    valor_unitario = db.Column(db.Float)
    qtd = db.Column(db.Integer)
    valor_total_itens = db.Column(db.Float)

    def to_json(self):
        return {
            'id': self.id,
            'pedido': self.pedido.id,
            'produto': self.produto.id,
            'valor_unitario': self.valor_unitario,
            'qtd': self.qtd,
            'valor_total_itens': self.valor_total_itens
        }

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(255))
    preco = db.Column(db.Float)
    categoria_id = db.Column(db.Integer(), db.ForeignKey('categoria.id'))
    categoria = db.relationship('categoria', backref = 'Categoria')
    #itemPedido = db.Column(db.Integer, db.ForeignKey('itemPedido.id')) #a mesma coisa aqui????

    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'preco': self.preco,
            'categoria': self.categoria
        }

class Categoria:
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(255))

    