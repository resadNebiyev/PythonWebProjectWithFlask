"""done

Revision ID: 7adc13eed073
Revises: 00231b8c98c3
Create Date: 2022-08-28 14:19:15.630619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7adc13eed073'
down_revision = '00231b8c98c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('info', sa.String(length=120), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category_items')
    # ### end Alembic commands ###
