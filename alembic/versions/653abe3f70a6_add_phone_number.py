"""add phone number

Revision ID: 653abe3f70a6
Revises: 759f9a697187
Create Date: 2023-05-10 16:33:32.812763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '653abe3f70a6'
down_revision = '759f9a697187'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
