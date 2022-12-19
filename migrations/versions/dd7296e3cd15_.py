"""empty message

Revision ID: dd7296e3cd15
Revises: 
Create Date: 2022-12-20 00:11:58.537587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd7296e3cd15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键'),
    sa.Column('name', sa.String(length=32), nullable=False, comment='用户名'),
    sa.Column('password', sa.String(length=32), nullable=True, comment='密码'),
    sa.Column('gender', sa.Integer(), nullable=False, comment='性别'),
    sa.Column('age', sa.Integer(), nullable=False, comment='年龄'),
    sa.Column('phone', sa.String(length=32), nullable=True, comment='电话号码'),
    sa.Column('email', sa.String(length=20), nullable=True, comment='邮箱'),
    sa.Column('isActive', sa.Boolean(), nullable=True, comment='是否活跃'),
    sa.Column('isAdmin', sa.Integer(), nullable=True),
    sa.Column('createTime', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('updateTime', sa.DateTime(), nullable=True, comment='修改时间'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###