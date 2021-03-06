"""empty message

Revision ID: 00b1fa3862ec
Revises: 
Create Date: 2021-10-11 18:24:40.041380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00b1fa3862ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('rating', sa.Integer(), nullable=True))
    op.alter_column('questions', 'category',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('category', 'questions', type_='foreignkey')
    op.create_foreign_key(None, 'questions', 'categories', ['category'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.create_foreign_key('category', 'questions', 'categories', ['category'], ['id'], onupdate='CASCADE', ondelete='SET NULL')
    op.alter_column('questions', 'category',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('questions', 'rating')
    # ### end Alembic commands ###
