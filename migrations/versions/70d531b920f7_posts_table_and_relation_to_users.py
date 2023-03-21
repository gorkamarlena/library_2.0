"""posts table and relation to users

Revision ID: 70d531b920f7
Revises: 6b98921ff8eb
Create Date: 2023-03-21 21:48:59.989484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70d531b920f7'
down_revision = '6b98921ff8eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_post_created'), ['created'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_post_created'))

    op.drop_table('post')
    # ### end Alembic commands ###
