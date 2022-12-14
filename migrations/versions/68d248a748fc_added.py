"""added

Revision ID: 68d248a748fc
Revises: e80a94f44bca
Create Date: 2022-09-03 15:04:18.792594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68d248a748fc'
down_revision = 'e80a94f44bca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('passward', sa.String(length=120), nullable=True),
    sa.Column('info', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
