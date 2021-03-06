"""empty message

Revision ID: 879544c3ca3f
Revises: 29cbca47c52a
Create Date: 2021-04-21 10:49:51.201581

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '879544c3ca3f'
down_revision = '29cbca47c52a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'role')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role', postgresql.ENUM('admin', 'supervisor', 'planner', 'worker', name='role_enum'), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
