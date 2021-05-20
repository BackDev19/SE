"""empty message

Revision ID: 816194ed80bc
Revises: 296b7c6b6540
Create Date: 2021-05-15 19:10:41.265740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '816194ed80bc'
down_revision = '296b7c6b6540'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_email'), type_='unique')

    # ### end Alembic commands ###