from sqlalchemy.sql import select, insert
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
#        ses = con.session()
#        ses.add(Countries.government(rank = "234"))
#        con.commit()
#        d["ids"] = 234
#        schema = government.CountriesSchema.load("",d)
        #d = schema().load(json.loads(json.dumps(data)))
#        print(schema)
#        print(data["Rank"])
#        print(d.type)
#        print(d.rank)
        stmt = (
        insert(government.Countries).values(d)
            #[data["Rank"], data["Country"], data["Revenues"], data["Expenditures"], data["SurplusDeficit"], data["SurplusGDP"], data["Year"]])
)
        print(stmt)
        result = con.execute(stmt)
        print("here here")
        print(result)
        return "Success"

