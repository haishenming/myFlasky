"""init db

Revision ID: 947cd1df123a
Revises: 
Create Date: 2017-09-07 10:54:02.891367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '947cd1df123a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'name', new_column_name='username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username', new_column_name='name')
    # ### end Alembic commands ###
