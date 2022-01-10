"""add content column to  post table

Revision ID: 457685863acd
Revises: 0a9b052fa12c
Create Date: 2022-01-08 19:35:39.060638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '457685863acd'
down_revision = '0a9b052fa12c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
