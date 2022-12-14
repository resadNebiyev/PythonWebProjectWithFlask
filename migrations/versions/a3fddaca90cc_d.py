"""d

Revision ID: a3fddaca90cc
Revises: 53d06f023493
Create Date: 2022-10-02 21:50:02.136952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3fddaca90cc'
down_revision = '53d06f023493'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_category'))
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('info', sa.Text(), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_events'))
    )
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('profession', sa.String(length=100), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.Column('info', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_member'))
    )
    op.create_table('navlinks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nav_Name', sa.String(length=200), nullable=True),
    sa.Column('nav_URL', sa.String(length=200), nullable=True),
    sa.Column('nav_order', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_navlinks'))
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('productName', sa.String(length=180), nullable=True),
    sa.Column('productPrice', sa.Integer(), nullable=True),
    sa.Column('producutInfo', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product'))
    )
    op.create_table('testimonials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('profession', sa.String(length=200), nullable=True),
    sa.Column('img', sa.String(length=200), nullable=True),
    sa.Column('info', sa.String(length=255), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_testimonials'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('passward', sa.String(length=100), nullable=True),
    sa.Column('info', sa.Text(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )
    op.create_table('category_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('info', sa.String(length=120), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], name=op.f('fk_category_items_category_id_category')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_category_items'))
    )
    op.create_table('member_img',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], name=op.f('fk_member_img_member_id_member')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_member_img'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('member_img')
    op.drop_table('category_items')
    op.drop_table('users')
    op.drop_table('testimonials')
    op.drop_table('product')
    op.drop_table('navlinks')
    op.drop_table('member')
    op.drop_table('events')
    op.drop_table('category')
    # ### end Alembic commands ###
