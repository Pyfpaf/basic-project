"""update users table

Revision ID: e834d2da0cf5
Revises: 2491cd1d0a42
Create Date: 2025-01-06 21:16:47.063925

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e834d2da0cf5"
down_revision: Union[str, None] = "2491cd1d0a42"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column("users", sa.Column("foo", sa.Integer(), nullable=False))
    op.add_column("users", sa.Column("bar", sa.Integer(), nullable=False))
    op.create_unique_constraint(
        op.f("uq_users_foo_bar"), "users", ["foo", "bar"]
    )


def downgrade() -> None:

    op.drop_constraint(op.f("uq_users_foo_bar"), "users", type_="unique")
    op.drop_column("users", "bar")
    op.drop_column("users", "foo")

