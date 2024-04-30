from main import db, relationship, ForeignKey, func

class Despesa(db.Model):
    id_despesa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_emissao = db.Column(db.Date)
    valor = db.Column(db.Integer)
    descricao = db.Column(db.String(256))
    nome_despesa = db.Column(db.String(256))
    id_usuario = db.Column(db.Integer, ForeignKey('usuario.id_usuario'))
    usuario = relationship("Usuario", back_populates="despesas")

class Receita(db.Model):
    id_receita = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_emissao = db.Column(db.Date)
    valor = db.Column(db.Integer)
    descricao = db.Column(db.String(256))
    nome_receita = db.Column(db.String(256))
    id_usuario = db.Column(db.Integer, ForeignKey('usuario.id_usuario'))
    usuario = relationship("Usuario", back_populates="receitas")

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(254))
    senha = db.Column(db.String(50))
    despesas = relationship("Despesa", back_populates="usuario")
    receitas = relationship("Receita", back_populates="usuario")