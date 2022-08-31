"""d

Revision ID: bdb9826ab831
Revises: 006669ae0a83
Create Date: 2022-08-28 18:14:40.955035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdb9826ab831'
down_revision = '006669ae0a83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_category_items_category_id_category'), 'category', ['category_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category_items', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_category_items_category_id_category'), type_='foreignkey')
        batch_op.drop_column('category_id')

    # ### end Alembic commands ###
