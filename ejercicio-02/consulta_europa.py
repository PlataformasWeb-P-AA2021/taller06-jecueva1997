from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from crear_base import Pais

engine = create_engine('sqlite:///datapersonas.db')

Session = sessionmaker(bind=engine)
session = Session()

paises = session.query(Pais).all() 

print("Presentar los países ordenados por la capital, siempre que el país pertenezca a Europa")
for i in paises:
    print("%s" % (i))

pais_europa = session.query(Pais).filter(Pais.nombre_pais=="EU").order_by(Pais.capital).all()
print(pais_europa)