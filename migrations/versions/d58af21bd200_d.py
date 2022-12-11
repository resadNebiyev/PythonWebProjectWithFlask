"""d

Revision ID: d58af21bd200
Revises: d88c685dec44
Create Date: 2022-11-20 21:42:02.395336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd58af21bd200'
down_revision = 'd88c685dec44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('enjoy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('price', sa.String(length=200), nullable=True),
    sa.Column('info', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_enjoy'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('enjoy')
    # ### end Alembic commands ###
