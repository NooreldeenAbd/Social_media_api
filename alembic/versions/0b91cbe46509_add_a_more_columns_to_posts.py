"""add a more columns to posts

Revision ID: 0b91cbe46509
Revises: 4e2aa228a152
Create Date: 2022-01-08 20:04:53.588598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b91cbe46509'
down_revision = '4e2aa228a152'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
                  sa.Column('pulished', sa.Boolean(), nullable=False,
                            server_default='True'))
    op.add_column('posts',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                            nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'punlished')
    op.drop_column('posts', 'created_at')
    pass
