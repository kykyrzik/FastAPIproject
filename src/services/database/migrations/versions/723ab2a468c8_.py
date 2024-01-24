"""empty message

Revision ID: 723ab2a468c8
Revises: d8d78dc2c072
Create Date: 2024-01-24 10:10:33.645964

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '723ab2a468c8'
down_revision: Union[str, None] = 'd8d78dc2c072'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
