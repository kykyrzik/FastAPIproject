"""empty message

Revision ID: 870426e0d6a9
Revises: f0d11c41d80a
Create Date: 2024-01-24 09:12:21.622232

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '870426e0d6a9'
down_revision: Union[str, None] = 'f0d11c41d80a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
