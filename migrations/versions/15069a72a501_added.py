"""added

Revision ID: 15069a72a501
Revises: 9b1d7f46b30d
Create Date: 2022-09-04 00:57:02.972188

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15069a72a501'
down_revision = '9b1d7f46b30d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('istifadeciler')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('istifadeciler',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), nullable=True),
    sa.Column('email', sa.VARCHAR(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_istifadeciler')
    )
    # ### end Alembic commands ###
