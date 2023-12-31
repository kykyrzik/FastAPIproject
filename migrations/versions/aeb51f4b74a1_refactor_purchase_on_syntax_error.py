"""refactor purchase on syntax error

Revision ID: aeb51f4b74a1
Revises: af151d88e833
Create Date: 2023-11-21 19:39:40.086280

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aeb51f4b74a1'
down_revision: Union[str, None] = 'af151d88e833'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('covertype', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.SMALLINT(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('covertype_id_seq'::regclass)"))
    op.alter_column('genre', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.SMALLINT(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('genre_id_seq'::regclass)"))
    op.alter_column('publisher', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.SMALLINT(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('publisher_id_seq'::regclass)"))
    op.alter_column('rars', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.SMALLINT(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('rars_id_seq'::regclass)"))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rars', 'id',
               existing_type=sa.SMALLINT(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('rars_id_seq'::regclass)"))
    op.alter_column('publisher', 'id',
               existing_type=sa.SMALLINT(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('publisher_id_seq'::regclass)"))
    op.alter_column('genre', 'id',
               existing_type=sa.SMALLINT(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('genre_id_seq'::regclass)"))
    op.alter_column('covertype', 'id',
               existing_type=sa.SMALLINT(),
               type_=sa.INTEGER(),
               existing_nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('covertype_id_seq'::regclass)"))
    # ### end Alembic commands ###
