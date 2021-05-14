from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from crear_base import Pais

engine = create_engine('sqlite:///datapersonas.db')

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all() 

print("Presentar todos los países del continente americano")
for i in paises:
    print("%s" % (i))

pais_continet = session.query(Pais).filter(Pais.continente=="NA").all()
print(pais_continet)