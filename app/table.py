from alembic import op
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import MetaData, Column, Integer, String, TIMESTAMP
import pymysql

#Aengine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
engine = create_engine("mariadb+pymysql://root:Qapla1999@192.168.1.94/government?charset=utf8mb4")
metadata = MetaData()

metadata.create_all(engine)

t_countries = Table(
    'countries', metadata,
    Column('Rank', String(3)),
    Column('Country', String(33)),
    Column('Revenues', String(8)),
    Column('Expenditures', String(8)),
    Column('Surplus..or.deficit.', String(10)),
    Column('Surplus.percentage.of.GDP', String(7)),
    Column('Year', String(21))
)

metadata.create_all(engine)

