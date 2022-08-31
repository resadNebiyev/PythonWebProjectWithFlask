"""done

Revision ID: 93400775574c
Revises: 707b5e348b16
Create Date: 2022-08-28 11:05:51.676370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93400775574c'
down_revision = '707b5e348b16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=True),
    sa.Column('number', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
