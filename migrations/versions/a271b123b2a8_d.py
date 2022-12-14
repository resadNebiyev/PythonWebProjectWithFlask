"""d

Revision ID: a271b123b2a8
Revises: 9c6a10c08e96
Create Date: 2022-12-03 23:58:30.817800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a271b123b2a8'
down_revision = '9c6a10c08e96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category_items', schema=None) as batch_op:
        batch_op.drop_column('img')

    # ### end Alembic commands ###
