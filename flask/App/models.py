from sqlalchemy import create_engine, Column, Date, Integer, ForeignKey, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///libros.db', echo=True)
Base = declarative_base()

# relaciones muchos a muchos
etiqueta_libro = Table('etiqueta_libro', Base.metadata,
    Column('libro_id', Integer, ForeignKey('libro.id')),
    Column('etiqueta_id', Integer, ForeignKey('etiqueta.id'))
)

autor_libro = Table('autor_libro', Base.metadata,
    Column('libro_id', Integer, ForeignKey('libro.id')),
    Column('autor_id', Integer, ForeignKey('autor.id'))
)


class Libro(Base):
    __tablename__ = 'libro'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(120), index=True, nullable=False)
    fecha_publicacion = Column(Date)
    isbn = Column(String(13))
    etiquetas = relationship("Etiqueta", secondary=etiqueta_libro)
    autores = relationship("Autor", secondary=autor_libro)

    def __init__(self, titulo, fecha_publicacion, isbn):
        self.titulo = titulo
        self.fecha_publicacion = fecha_publicacion
        self.isbn = isbn

    def __str__(self):
        return  self.titulo


class Etiqueta(Base):
    __tablename__ = 'etiqueta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre

class Autor(Base):
    __tablename__ = 'autor'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)