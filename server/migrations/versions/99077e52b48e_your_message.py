"""your message

Revision ID: 99077e52b48e
Revises: 
Create Date: 2025-06-19 13:15:59.990450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99077e52b48e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
