from sqlalchemy import create_engine
from sqlalchemy.sql.sqltypes import Float

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///datapersonas.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'lospaises'
    
    id = Column(Integer, primary_key=True)
    nombre_pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname_id = Column(String)
    itu = Column(String)
    languajes = Column(String) 
    independiente = Column(String)
 
    def __repr__(self):
        return "Pais: nombre_pais: %s capital: %s continente: %s dial: %s geoname_id: %s itu: %s languajes: %s independiente: %s" % (
                         self.nombre_pais,
                        self.capital, 
                        self.continente,
                        self.dial,
                        self.geoname_id,
                        self.itu,
                        self.languajes,
                        self.independiente)

            
                        
     
       
Base.metadata.create_all(engine)