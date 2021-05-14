from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from crear_base import Pais

engine = create_engine('sqlite:///datapersonas.db')

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all() 

print("Presentar los lenguajes de cada país")
for i in paises:
    print("%s" % (i))

pais_languaje = session.query(Pais).filter(Pais.nombre_pais, Pais.languajes).all()
print(pais_languaje)