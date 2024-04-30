from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from view import *
from models import Usuario, Despesa, Receita

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)