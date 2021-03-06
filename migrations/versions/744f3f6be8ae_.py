"""empty message

Revision ID: 744f3f6be8ae
Revises: 
Create Date: 2022-02-08 01:30:21.865867

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '744f3f6be8ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('catalog', sa.Column('userid', sa.Integer(), nullable=True))
    op.drop_index('username', table_name='catalog')
    op.drop_column('catalog', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('catalog', sa.Column('username', mysql.VARCHAR(length=150), nullable=True))
    op.create_index('username', 'catalog', ['username'], unique=False)
    op.drop_column('catalog', 'userid')
    # ### end Alembic commands ###
