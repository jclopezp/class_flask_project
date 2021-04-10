import datetime
from flask_sqlalchemy import SQLAlchemy

# init our DB
db = SQLAlchemy()

class BootcampModel (db.Model):

    __tablename__ = 'bootcamp'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)

    # Relations
    generations = db.relationship('GenerationModel', backref='bootcamp', lazy=True) # Lazy la forma en como traes la informacion

    def __init__(self, data):
        """Contsructor. """
        self.name = data.get("name")
        self.created_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod # tipo de metodo
    def get_all():
        return BootcampModel.query.all()

    def __repr__(self):
        return f'<Bootcamp: {self.name}>'

class GenerationModel (db.Model):

    __tablename__ = 'generation'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime)

    # Relations
    bootcamp_id = db.Column(db.Integer, db.ForeignKey("bootcamp.id"), nullable=False)

    def __init__(self, data):
        """Contsructor. """
        self.number = data.get("number")
        self.created_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Generartion: {self.number}>'

    
    