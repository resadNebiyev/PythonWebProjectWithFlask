"""done

Revision ID: e63885f36d56
Revises: 8e68347d54df
Create Date: 2022-08-23 01:21:33.487233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e63885f36d56'
down_revision = '8e68347d54df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('testimonials', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('testimonials', 'is_active')
    # ### end Alembic commands ###
