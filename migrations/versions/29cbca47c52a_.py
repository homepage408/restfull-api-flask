"""empty message

Revision ID: 29cbca47c52a
Revises: 09800a6f86cf
Create Date: 2021-04-21 10:36:31.720144

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '29cbca47c52a'
down_revision = '09800a6f86cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('status', postgresql.ENUM('approve', 'submit', 'reject', name='status_enum'), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
