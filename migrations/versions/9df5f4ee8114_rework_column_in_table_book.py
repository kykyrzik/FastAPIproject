"""rework column in table book

Revision ID: 9df5f4ee8114
Revises: c517e9defa57
Create Date: 2023-11-24 19:06:27.890087

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9df5f4ee8114'
down_revision: Union[str, None] = 'c517e9defa57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('ISBN', sa.VARCHAR(length=17), nullable=False),
    sa.Column('name_book', sa.VARCHAR(length=50), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.SMALLINT(), nullable=False),
    sa.Column('publisher_id', sa.SMALLINT(), nullable=False),
    sa.Column('publication_date', sa.Integer(), nullable=True),
    sa.Column('book_circulation', sa.Integer(), nullable=True),
    sa.Column('unit_price', sa.DECIMAL(precision=4, scale=2), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('rars_id', sa.SMALLINT(), nullable=False),
    sa.Column('number_of_pages', sa.Integer(), nullable=False),
    sa.Column('cover_type_id', sa.Integer(), nullable=False),
    sa.Column('amount_book', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['cover_type_id'], ['cover.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['publisher_id'], ['publisher.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['rars_id'], ['rars.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('ISBN')
    )
    op.create_index(op.f('ix_book_name_book'), 'book', ['name_book'], unique=False)
    op.alter_column('genre', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.SMALLINT(),
               existing_nullable=False,
               autoincrement=True)
    op.create_foreign_key(None, 'item', 'book', ['book_id'], ['ISBN'], ondelete='CASCADE')
    op.alter_column('publisher', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.SMALLINT(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('rars', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.SMALLINT(),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rars', 'id',
               existing_type=sa.SMALLINT(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('publisher', 'id',
               existing_type=sa.SMALLINT(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True)
    op.drop_constraint(None, 'item', type_='foreignkey')
    op.alter_column('genre', 'id',
               existing_type=sa.SMALLINT(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True)
    op.drop_index(op.f('ix_book_name_book'), table_name='book')
    op.drop_table('book')
    # ### end Alembic commands ###