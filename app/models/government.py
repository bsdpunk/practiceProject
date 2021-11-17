from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

ma = Marshmallow()
Base = declarative_base()



class Countries(Base):
    __tablename__ = "countries"
    ids = Column('id', Integer, primary_key = True)
    rank = Column('Rank', String(3))
    country = Column('Country', String(33))
    revenues = Column('Revenues', String(8))
    expenditures = Column('Expenditures', String(8))
    surplusDeficit = Column('SurplusDeficit', String(10))
    surplusGDP = Column('SurplusGDP', String(7))
    year = Column('Year', String(21))



class CountriesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Countries
        fields = ( "Rank", "Country", "Revenues", "Expenditures", "SurplusDeficit", "SurplusGDP", "Year")
        include_fk = True
        load_instance = True
    ids = ma.auto_field()
    rank = ma.auto_field()
    country = ma.auto_field()
    revenues = ma.auto_field()
    expenditures = ma.auto_field()
    surplusDeficit = ma.auto_field()
    surplusGDP = ma.auto_field()
    year = ma.auto_field()

