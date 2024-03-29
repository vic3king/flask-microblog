"""new fields in user model

Revision ID: c52d0ac305f9
Revises: 93d39ef13d49
Create Date: 2019-08-21 21:25:32.029021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c52d0ac305f9'
down_revision = '93d39ef13d49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('post', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'last_seen')
    op.drop_column('post', 'about_me')
    # ### end Alembic commands ###
