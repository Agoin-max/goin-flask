"""empty message

Revision ID: 65a7fe156452
Revises: 70b2031d3a39
Create Date: 2022-12-22 17:37:14.862424

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '65a7fe156452'
down_revision = '70b2031d3a39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('debit_currency', schema=None) as batch_op:
        batch_op.alter_column('max_amount',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.DECIMAL(),
               existing_comment='最多可借额度',
               existing_nullable=False)
        batch_op.alter_column('min_amount',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.DECIMAL(),
               existing_comment='最少可借额度',
               existing_nullable=False)
        batch_op.alter_column('rate',
               existing_type=mysql.VARCHAR(length=10),
               type_=sa.DECIMAL(),
               existing_comment='利率',
               existing_nullable=False)
        batch_op.alter_column('over_rate',
               existing_type=mysql.VARCHAR(length=10),
               type_=sa.DECIMAL(),
               existing_comment='逾期利率',
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('debit_currency', schema=None) as batch_op:
        batch_op.alter_column('over_rate',
               existing_type=sa.DECIMAL(),
               type_=mysql.VARCHAR(length=10),
               existing_comment='逾期利率',
               existing_nullable=False)
        batch_op.alter_column('rate',
               existing_type=sa.DECIMAL(),
               type_=mysql.VARCHAR(length=10),
               existing_comment='利率',
               existing_nullable=False)
        batch_op.alter_column('min_amount',
               existing_type=sa.DECIMAL(),
               type_=mysql.VARCHAR(length=20),
               existing_comment='最少可借额度',
               existing_nullable=False)
        batch_op.alter_column('max_amount',
               existing_type=sa.DECIMAL(),
               type_=mysql.VARCHAR(length=20),
               existing_comment='最多可借额度',
               existing_nullable=False)

    # ### end Alembic commands ###
