"""empty message

Revision ID: 264223f21244
Revises: 723ab2a468c8
Create Date: 2024-01-24 10:11:41.654753

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '264223f21244'
down_revision: Union[str, None] = '723ab2a468c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
