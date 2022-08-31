"""done

Revision ID: f1e1410ebfcb
Revises: 
Create Date: 2022-08-20 14:05:03.693205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1e1410ebfcb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('productName', sa.VARCHAR(length=180), nullable=True),
    sa.Column('productPrice', sa.INTEGER(), nullable=True),
    sa.Column('producutInfo', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
