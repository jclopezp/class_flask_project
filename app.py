from flask import Flask

from src.models import db
from src.views import bootcamp_api

app = Flask(__name__)

# configuramos la DB en la APP
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:123456@localhost:5432/bootcamp"

app.register_blueprint(bootcamp_api, url_prefix='/api/bootcamps/')

# Para que la BD maneja toda la info de la APP
from src.models import *
db.init_app(app)
db.app = app
#db.create_all()

@app.route("/")
def hola_mundo():
    return "Hola mundo"
