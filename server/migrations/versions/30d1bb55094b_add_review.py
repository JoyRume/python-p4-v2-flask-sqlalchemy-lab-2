"""add review

Revision ID: 30d1bb55094b
Revises: 5a88c0ad1853
Create Date: 2024-04-05 18:46:59.993226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30d1bb55094b'
down_revision = '5a88c0ad1853'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('price', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'price')
    # ### end Alembic commands ###
