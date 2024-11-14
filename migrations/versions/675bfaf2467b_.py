"""empty message

Revision ID: 675bfaf2467b
Revises: 1f995ac9ba0a
Create Date: 2024-05-23 08:52:35.774831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '675bfaf2467b'
down_revision = '1f995ac9ba0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_comentarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=True),
    sa.Column('comentario', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_comentarios')
    # ### end Alembic commands ###
