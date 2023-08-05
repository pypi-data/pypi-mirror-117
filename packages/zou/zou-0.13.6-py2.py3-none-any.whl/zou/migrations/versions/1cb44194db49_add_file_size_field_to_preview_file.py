"""add file size field to preview file

Revision ID: 1cb44194db49
Revises: cf6cec6d6bf5
Create Date: 2021-01-20 10:58:07.202278

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '1cb44194db49'
down_revision = 'cf6cec6d6bf5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('preview_file', sa.Column('file_size', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('preview_file', 'file_size')
    # ### end Alembic commands ###
