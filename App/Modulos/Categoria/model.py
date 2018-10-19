from App import db

class Categoria(db.Model):
    __tablename__='categoria'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    Nombre = db.Column(db.String(15), nullable=False)



