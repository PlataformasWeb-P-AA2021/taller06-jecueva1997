from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from crear_base import Pais

engine = create_engine('sqlite:///datapersonas.db')

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all() 

print("Presentar todos los países que tengan en su cadena de nombre de país 'uador' o en su cadena de capital 'ito'.")
for i in paises:
    print("%s" % (i))



pais_terminacion = session.query(Pais).filter(or_(Pais.nombre_pais.like("%uador%"), Pais.capital.like("%ito%"))).all()
print(pais_terminacion)