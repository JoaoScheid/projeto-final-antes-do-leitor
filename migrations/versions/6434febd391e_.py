"""empty message

Revision ID: 6434febd391e
Revises: aa0476ccec4e
Create Date: 2024-08-15 09:35:42.609706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6434febd391e'
down_revision = 'aa0476ccec4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('material_movimentacao', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tipo_produto', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('material_movimentacao', schema=None) as batch_op:
        batch_op.drop_column('tipo_produto')

    # ### end Alembic commands ###