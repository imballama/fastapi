"""Add user table

Revision ID: 1deb4024cc0c
Revises: b8d71f76e54c
Create Date: 2023-05-10 11:00:31.716913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1deb4024cc0c'
down_revision = 'b8d71f76e54c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
