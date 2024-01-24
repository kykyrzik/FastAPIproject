"""empty message

Revision ID: c1abee5659ac
Revises: c67afe066d5d
Create Date: 2024-01-24 09:19:20.170536

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1abee5659ac'
down_revision: Union[str, None] = 'c67afe066d5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
