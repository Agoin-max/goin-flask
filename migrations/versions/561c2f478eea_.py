"""empty message

Revision ID: 561c2f478eea
Revises: ff943223984f
Create Date: 2022-12-22 16:35:52.301232

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '561c2f478eea'
down_revision = 'ff943223984f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=32),
               type_=sa.String(length=256),
               existing_comment='密码',
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=256),
               type_=mysql.VARCHAR(length=32),
               existing_comment='密码',
               existing_nullable=True)

    # ### end Alembic commands ###