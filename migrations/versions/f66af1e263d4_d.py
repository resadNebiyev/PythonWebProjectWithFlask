"""d

Revision ID: f66af1e263d4
Revises: 2ba48ffa587d
Create Date: 2022-12-04 16:14:58.072266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f66af1e263d4'
down_revision = '2ba48ffa587d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('info2', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category_items', schema=None) as batch_op:
        batch_op.drop_column('info2')

    # ### end Alembic commands ###
