"""d

Revision ID: 63b178d17bb5
Revises: 799127ef37df
Create Date: 2022-11-18 22:42:21.493118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63b178d17bb5'
down_revision = '799127ef37df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    op.drop_table('member_img')
    op.drop_table('navlinks')
    op.drop_table('category_items')
    op.drop_table('testimonials')
    op.drop_table('product')
    op.drop_table('category')
    op.drop_table('users')
    op.drop_table('recommends')
    op.drop_table('abouts')
    op.drop_table('member')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('profession', sa.VARCHAR(length=100), nullable=True),
    sa.Column('img', sa.VARCHAR(length=100), nullable=True),
    sa.Column('info', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_member')
    )
    op.create_table('abouts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('img', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_abouts')
    )
    op.create_table('recommends',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('number', sa.INTEGER(), nullable=True),
    sa.Column('title', sa.VARCHAR(length=150), nullable=True),
    sa.Column('text', sa.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_recommends')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), nullable=True),
    sa.Column('email', sa.VARCHAR(length=150), nullable=True),
    sa.Column('passward', sa.VARCHAR(length=100), nullable=True),
    sa.Column('info', sa.TEXT(), nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_users')
    )
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('order', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_category')
    )
    op.create_table('product',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('productName', sa.VARCHAR(length=180), nullable=True),
    sa.Column('productPrice', sa.INTEGER(), nullable=True),
    sa.Column('producutInfo', sa.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_product')
    )
    op.create_table('testimonials',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=200), nullable=True),
    sa.Column('profession', sa.VARCHAR(length=200), nullable=True),
    sa.Column('img', sa.VARCHAR(length=200), nullable=True),
    sa.Column('info', sa.VARCHAR(length=255), nullable=True),
    sa.Column('order', sa.INTEGER(), nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_testimonials')
    )
    op.create_table('category_items',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), nullable=True),
    sa.Column('info', sa.VARCHAR(length=120), nullable=True),
    sa.Column('price', sa.INTEGER(), nullable=True),
    sa.Column('category_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], name='fk_category_items_category_id_category'),
    sa.PrimaryKeyConstraint('id', name='pk_category_items')
    )
    op.create_table('navlinks',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('nav_Name', sa.VARCHAR(length=200), nullable=True),
    sa.Column('nav_URL', sa.VARCHAR(length=200), nullable=True),
    sa.Column('nav_order', sa.INTEGER(), nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_navlinks')
    )
    op.create_table('member_img',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('member_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], name='fk_member_img_member_id_member'),
    sa.PrimaryKeyConstraint('id', name='pk_member_img')
    )
    op.create_table('events',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=120), nullable=True),
    sa.Column('price', sa.INTEGER(), nullable=True),
    sa.Column('info', sa.TEXT(), nullable=True),
    sa.Column('img', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_events')
    )
    # ### end Alembic commands ###
