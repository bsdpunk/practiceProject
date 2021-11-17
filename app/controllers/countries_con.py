from sqlalchemy.sql import select, insert, delete, update
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
import sys
sys.path.insert(1, '/app/models')
import government
import pymysql
import json

def asdict(i):
    return {'rank': i.Rank,
            'country': i.Country, 
            'revenues': i.Revenues,
            'expenditures': i.Expenditures,  
            'Year': i.Year}


con = create_engine('mysql+pymysql://root:Qapla1999@192.168.1.94/government', echo=True)
session = scoped_session(sessionmaker(bind=con))
class Country_con:
    def select(self, ids = None):
        if ids == None:
            ids = 0
            s = select(government.Countries)
            result = con.execute(s)
            i = result.fetchall()
            ids = int(ids)
            master = {}
            for row in i:
                master[row.id] = asdict(row)
            return master
        else:
            s = select(government.Countries).where(government.Countries.ids == ids)
            print(s)
            result = con.execute(s).fetchone()
            return asdict(result)

    def ins(self, data):
        d = json.loads(json.dumps(data))
        print(d["Rank"])
        schema = government.CountriesSchema()
        g = government.Countries(rank = d["Rank"], country=d["Country"] ,
                year=d["Year"], revenues = d["Revenues"],
                expenditures=d["Expenditures"], surplusGDP = d["SurplusGDP"], 
                surplusDeficit = d["SurplusDeficit"])
        session.add(g)
        session.commit()
        print(schema.dump(schema))


        
#        r = json.dumps(data)
#        schema = government.CountriesSchema(many=True)
#        d = schema().loads(d)
#        print("--------")
#        print(d)
#        s = schema(many=True)
#        d = s.load(dict(d))
#        session.add(d)
#        session.commit()
#        stmt = (
#        insert(government.Countries).values(d)
#)
        #print(stmt)
#        result = con.execute(stmt)
#        print(result)
        return "Success"
    
    def updash(self, ids, data):
        d = json.loads(json.dumps(data))
        schema = government.CountriesSchema()
#        g = government.Countries(ids= ids, 
#                rank = d["Rank"], 
#                country=d["Country"] ,
#                year=d["Year"], 
#                revenues = d["Revenues"],
#                expenditures=d["Expenditures"], 
#                surplusGDP = d["SurplusGDP"], 
#                surplusDeficit = d["SurplusDeficit"]
#                )
#        session.query(User).filter(User.name == "squidward").\
#        update({"name": "spongebob"}, synchronize_session="fetch")
#        session.update(g)
#        session.commit()




        stmt = (
        update(government.Countries).values(d).where(government.Countries.ids == ids)
        )
        result = con.execute(stmt)
        #print(schema.dump(schema))
        return "Success"
    
    def remove(self, ids):
        print(ids)
        stmt = (
        delete(government.Countries).where(government.Countries.ids == ids)
        )
        result = con.execute(stmt)
        return "Success"
