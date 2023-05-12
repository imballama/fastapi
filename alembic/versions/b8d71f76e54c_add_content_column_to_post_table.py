"""add content column to post table

Revision ID: b8d71f76e54c
Revises: 4a9ee3a5c66e
Create Date: 2023-05-10 10:54:48.090259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8d71f76e54c'
down_revision = '4a9ee3a5c66e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('content', sa.String(), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
