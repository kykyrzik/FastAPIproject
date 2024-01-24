"""empty message

Revision ID: f0d11c41d80a
Revises: b501628138e6
Create Date: 2024-01-24 07:20:03.387483

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f0d11c41d80a'
down_revision: Union[str, None] = 'b501628138e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
