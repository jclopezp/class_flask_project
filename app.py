from flask import Flask

from src.models import db

app = Flask(__name__)

# configuramos la DB en la APP
app.config['SQLALCHEMY_DATBASE_URI'] = "postgresql://admin:123456@localhost:5432/bootcamp"

# PAra que la BD maneja toda la info de la APP
db.init_app(app)
db.app = app
db.create_all()

@app.route("/")
def hola_mundo():
    return "Hola mundo"
