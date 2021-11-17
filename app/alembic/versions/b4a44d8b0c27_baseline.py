"""baseline

Revision ID: b4a44d8b0c27
Revises: 
Create Date: 2021-11-17 15:27:31.445755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4a44d8b0c27'
down_revision = None
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
