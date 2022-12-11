"""d

Revision ID: 2eedd889c129
Revises: d58af21bd200
Create Date: 2022-11-20 21:56:52.471565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2eedd889c129'
down_revision = 'd58af21bd200'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('enjoy', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('enjoy', schema=None) as batch_op:
        batch_op.drop_column('img')

    # ### end Alembic commands ###
