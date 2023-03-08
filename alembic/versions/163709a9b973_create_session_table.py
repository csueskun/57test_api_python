"""create session table

Revision ID: 163709a9b973
Revises: 7c89e00d9543
Create Date: 2023-03-07 18:18:09.784645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '163709a9b973'
down_revision = '7c89e00d9543'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('session',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('token', sa.String(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('session')
