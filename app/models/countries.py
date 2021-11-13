from sqlalchemy import Column, MetaData, String, Table

metadata = MetaData()


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
