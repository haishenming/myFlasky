"""empty message

Revision ID: b1f749dbc47d
Revises: 2a77a8c5c4cd
Create Date: 2017-09-07 17:17:36.145365

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite


# revision identifiers, used by Alembic.
revision = 'b1f749dbc47d'
down_revision = '2a77a8c5c4cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'name', new_column_name='username',
                    existing_type=sqlite.VARCHAR(length=64))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username', new_column_name='name',
                    existing_type=sqlite.VARCHAR(length=64))
    # ### end Alembic commands ###