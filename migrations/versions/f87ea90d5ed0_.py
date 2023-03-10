"""empty message

Revision ID: f87ea90d5ed0
Revises: f36227b1e639
Create Date: 2022-12-22 19:32:04.019785

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f87ea90d5ed0'
down_revision = 'f36227b1e639'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('debit_user',
    sa.Column('createTime', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('updateTime', sa.DateTime(), nullable=True, comment='修改时间'),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键'),
    sa.Column('amount', sa.DECIMAL(precision=25, scale=8), nullable=True, comment='可用额度'),
    sa.Column('borrowing_times', sa.Integer(), nullable=True, comment='借款次数'),
    sa.Column('used', sa.DECIMAL(precision=25, scale=8), nullable=True, comment='已使用'),
    sa.Column('user_id', sa.Integer(), nullable=False, comment='用户ID'),
    sa.Column('currency_id', sa.Integer(), nullable=False, comment='币种ID'),
    sa.ForeignKeyConstraint(['currency_id'], ['currency.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('debit_user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_debit_user_currency_id'), ['currency_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_debit_user_user_id'), ['user_id'], unique=False)

    with op.batch_alter_table('currency', schema=None) as batch_op:
        batch_op.alter_column('currency_name',
               existing_type=mysql.VARCHAR(length=32),
               comment='币种名称',
               existing_comment='货币名称',
               existing_nullable=False)
        batch_op.alter_column('icon',
               existing_type=mysql.VARCHAR(length=50),
               comment='币种图标',
               existing_comment='货币图标',
               existing_nullable=True)

    with op.batch_alter_table('debit_currency', schema=None) as batch_op:
        batch_op.alter_column('currency_id',
               existing_type=mysql.INTEGER(),
               comment='币种ID',
               existing_comment='货币ID',
               existing_nullable=False)
        batch_op.create_index(batch_op.f('ix_debit_currency_currency_id'), ['currency_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('debit_currency', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_debit_currency_currency_id'))
        batch_op.alter_column('currency_id',
               existing_type=mysql.INTEGER(),
               comment='货币ID',
               existing_comment='币种ID',
               existing_nullable=False)

    with op.batch_alter_table('currency', schema=None) as batch_op:
        batch_op.alter_column('icon',
               existing_type=mysql.VARCHAR(length=50),
               comment='货币图标',
               existing_comment='币种图标',
               existing_nullable=True)
        batch_op.alter_column('currency_name',
               existing_type=mysql.VARCHAR(length=32),
               comment='货币名称',
               existing_comment='币种名称',
               existing_nullable=False)

    with op.batch_alter_table('debit_user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_debit_user_user_id'))
        batch_op.drop_index(batch_op.f('ix_debit_user_currency_id'))

    op.drop_table('debit_user')
    # ### end Alembic commands ###
