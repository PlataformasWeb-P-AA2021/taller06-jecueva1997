from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_base import Pais

import json
import requests


engine = create_engine('sqlite:///datapersonas.db')

Session = sessionmaker(bind=engine)
session = Session()

archivo = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")

json_data = (archivo.json())
for i in json_data:
    print(i)
    p = Pais(nombre_pais=i['CLDR display name'], capital=i['Capital'], continente=i['Continent'], \
            dial=i["Dial"], geoname_id=i['Geoname ID'], itu=i["ITU"], languajes=i["Languages"], \
                independiente=i["is_independent"])
    session.add(p)
 
    #print(i["CLDR display name"])
    #print(i["Capital"])
    #print(i["Continent"])
    #print(i["Dial"])
    #print(i["Geoname ID"])
    #print(i["ITU"])
    #print(i["Languages"])
    #print(i["is_independent"])


session.commit()


