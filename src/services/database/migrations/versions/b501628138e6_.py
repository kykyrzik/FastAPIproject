"""empty message

Revision ID: b501628138e6
Revises: adf7335ac625
Create Date: 2024-01-24 07:17:54.920996

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b501628138e6'
down_revision: Union[str, None] = 'adf7335ac625'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
