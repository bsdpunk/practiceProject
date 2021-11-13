"""baseline

Revision ID: 3b3540e80e88
Revises: a28434f83abf
Create Date: 2021-11-13 22:33:07.721084

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3b3540e80e88'
down_revision = 'a28434f83abf'
branch_labels = None
depends_on = None


alembic upgrade --sqldef upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('countries2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    # ### end Alembic commands ###
