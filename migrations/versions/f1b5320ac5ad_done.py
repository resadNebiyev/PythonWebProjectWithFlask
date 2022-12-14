"""done

Revision ID: f1b5320ac5ad
Revises: f1e1410ebfcb
Create Date: 2022-08-22 15:19:17.427695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1b5320ac5ad'
down_revision = 'f1e1410ebfcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('NEW_MODEL',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('m_Name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('productName', sa.String(length=180), nullable=True),
    sa.Column('productPrice', sa.Integer(), nullable=True),
    sa.Column('producutInfo', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('NEW_MODEL')
    # ### end Alembic commands ###
