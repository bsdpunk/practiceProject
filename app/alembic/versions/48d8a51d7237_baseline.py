"""baseline

Revision ID: 48d8a51d7237
Revises: 5a3e6a44adef
Create Date: 2021-11-17 00:49:25.274482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48d8a51d7237'
down_revision = '5a3e6a44adef'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('countries',
    sa.Column('id', sa.Integer, primary_key = True),
    sa.Column('Rank', sa.String(3)),
    sa.Column('Country', sa.String(33)),
    sa.Column('Revenues', sa.String(8)),
    sa.Column('Expenditures', sa.String(8)),
    sa.Column('SurplusDeficit', sa.String(10)),
    sa.Column('SurplusGDP', sa.String(7)),
    sa.Column('Year', sa.String(21)),        
    )
    
def downgrade():
        op.drop_table('countries')
