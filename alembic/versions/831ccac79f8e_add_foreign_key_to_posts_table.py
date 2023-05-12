"""add foreign-key to posts table

Revision ID: 831ccac79f8e
Revises: 1deb4024cc0c
Create Date: 2023-05-10 13:05:12.935129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '831ccac79f8e'
down_revision = '1deb4024cc0c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer(), nullable=False)
    )
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'],
                          remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
