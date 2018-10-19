from App import db

class Clientes(db.Model):
    __tablename__ = "Cliente"
    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Apellido = db.Column(db.String(50))

    def as_dict(self):
        dic={'Id': self.id,
        'Nombre': self.Nombre,
        'Apellido': self.Apellido,
        'FechaNacimiento': self.FechaNacimiento
        }
        return dic

