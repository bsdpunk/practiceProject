"""baseline

Revision ID: a28434f83abf
Revises: 5591001e21c3
Create Date: 2021-11-13 22:02:16.594264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a28434f83abf'
down_revision = '5591001e21c3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'countries2',
        sa.Column('id', sa.Integer, primary_key=True),  
        sa.Column('Rank', sa.String(3)),
        sa.Column('Country', sa.String(33)),
        sa.Column('Revenues', sa.String(8)),
        sa.Column('Expenditures', sa.String(8)),
        sa.Column('Surplus..or.deficit.', sa.String(10)),
        sa.Column('Surplus.percentage.of.GDP', sa.String(7)),
        sa.Column('Year', sa.String(21)))


def downgrade():
    op.drop_table('countries')
    pass
