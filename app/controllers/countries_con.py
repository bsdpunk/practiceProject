from sqlalchemy.sql import select, insert, delete, update
from sqlalchemy import create_engine
import sys
sys.path.insert(1, '/app/models')
import government
import pymysql
import json
print(government)

def asdict(i):
    return {'rank': i.Rank, 'country': i.Country, 'revenues': i.Revenues,
            'expenditures': i.Expenditures,  'Year': i.Year}

con = create_engine('mysql+pymysql://root:Qapla1999@192.168.1.94/government', echo=True)
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
#        schema = government.CountriesSchema.load("",d)
        #d = schema().load(json.loads(json.dumps(data)))
        stmt = (
        insert(government.Countries).values(d)
)
        print(stmt)
        result = con.execute(stmt)
        print("here here")
        print(result)
        return "Success"
    def updash(self, ids, data):
        d = json.loads(json.dumps(data))
        stmt = (
        update(government.Countries).values(d).where(government.Countries.ids == ids)
        )
        result = con.execute(stmt)
        return "Success"
    def remove(self, ids):
        print(ids)
        stmt = (
        delete(government.Countries).where(government.Countries.ids == ids)
        )
        result = con.execute(stmt)
        return "Success"
