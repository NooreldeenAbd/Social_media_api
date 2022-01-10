"""add foreign-key to post table

Revision ID: 4e2aa228a152
Revises: 0bb7e04ab9a6
Create Date: 2022-01-08 19:49:59.495517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e2aa228a152'
down_revision = '0bb7e04ab9a6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'post_users_fk', source_table='posts', referent_table='users',
        local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
