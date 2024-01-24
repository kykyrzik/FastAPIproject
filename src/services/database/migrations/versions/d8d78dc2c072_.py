"""empty message

Revision ID: d8d78dc2c072
Revises: c1abee5659ac
Create Date: 2024-01-24 10:05:46.950554

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8d78dc2c072'
down_revision: Union[str, None] = 'c1abee5659ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
