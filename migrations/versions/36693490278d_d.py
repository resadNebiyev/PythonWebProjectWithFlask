"""d

Revision ID: 36693490278d
Revises: 7adc13eed073
Create Date: 2022-08-28 17:27:59.013751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36693490278d'
down_revision = '7adc13eed073'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('category_items', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('category_items', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
