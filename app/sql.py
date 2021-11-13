from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import MetaData, Column, Integer, String, TIMESTAMP
import pymysql
#Aengine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
engine = create_engine("mariadb+pymysql://root:Qapla1999@192.168.1.94/crime?charset=utf8mb4")
metadata = MetaData()
Table('mytable', metadata,
      Column('data', String(32)),
      mysql_engine='InnoDB',
      mysql_charset='utf8mb4',
      mysql_key_block_size="1024"
     )

metadata.create_all(engine)
