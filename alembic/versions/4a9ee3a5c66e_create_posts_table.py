"""create posts table

Revision ID: 4a9ee3a5c66e
Revises: 
Create Date: 2023-05-10 10:42:42.777064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a9ee3a5c66e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
    )

    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
