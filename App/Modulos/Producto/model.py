from App import db

class productos(db.Model):
    __tablename__='Productos'
    Codigo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    Precio = db.Column(db.Numeric)
    stock = db.Column(db.Numeric)
    Categoria= db.Column(db.Integer,db.ForeignKey("categoria.id"),nullable=False)
    categori=db.relationship('Categoria', backref=db.backref('Productos',lazy=True))
    
    def __relp__(self):
        return '{0}'.format(self.Codigo)

