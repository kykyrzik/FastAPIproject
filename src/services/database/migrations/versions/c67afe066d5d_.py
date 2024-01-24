"""empty message

Revision ID: c67afe066d5d
Revises: 870426e0d6a9
Create Date: 2024-01-24 09:16:25.535752

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c67afe066d5d'
down_revision: Union[str, None] = '870426e0d6a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
