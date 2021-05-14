from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from crear_base import Pais
 
engine = create_engine('sqlite:///datapersonas.db')

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all() 

print("Presentar los países de Asía, ordenados por el atributo Dial.")
for i in paises:
    print("%s" % (i))

pais_asia = session.query(Pais).filter(Pais.continente=="AS").order_by(Pais.dial).all()
print(pais_asia)