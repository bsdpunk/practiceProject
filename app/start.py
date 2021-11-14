from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql




    op.create_table('countries',
        sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
        sa.Column('Rank', mysql.VARCHAR(length=3), nullable=True),
        sa.Column('Country', mysql.VARCHAR(length=33), nullable=True),
        sa.Column('Revenues', mysql.VARCHAR(length=8), nullable=True),
        sa.Column('Expenditures', mysql.VARCHAR(length=8), nullable=True),
        sa.Column('Surplus..or.deficit.', mysql.VARCHAR(length=10), nullable=True),
        sa.Column('Surplus.percentage.of.GDP', mysql.VARCHAR(length=7), nullable=True),
        sa.Column('Year', mysql.VARCHAR(length=21), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_default_charset='utf8mb4',
        mysql_engine='InnoDB'
        )

    import json

new_record = ModelName(
    name='Foo',
    data1=open('./filename.json').read(),
    data2=json.dumps(open('./filename.json').read(), indent=2)
)
try:
    db.session.add(new_record)
    db.session.commit()
    print('Insert successful')
except:
    print('Insert failed')
