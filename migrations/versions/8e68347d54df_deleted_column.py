"""deleted column

Revision ID: 8e68347d54df
Revises: 4955b883fb3a
Create Date: 2022-08-22 16:11:49.446513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e68347d54df'
down_revision = '4955b883fb3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('testimonials', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('testimonials', sa.Column('is_active', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###
