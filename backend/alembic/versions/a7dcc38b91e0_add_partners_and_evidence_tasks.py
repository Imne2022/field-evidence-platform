"""add partners and evidence_tasks

Revision ID: a7dcc38b91e0
Revises: 94731472524b
Create Date: 2026-10-01 17:19:54.249493

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a7dcc38b91e0"
down_revision: Union[str, Sequence[str], None] = "94731472524b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create partners and evidence_tasks tables."""

    op.create_table(
        "partners",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("display_name", sa.String(length=120), nullable=False),
        sa.Column("level", sa.String(length=20), nullable=False),
        sa.Column("qa_pass_rate", sa.Float(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "evidence_tasks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("incident_id", sa.Integer(), nullable=False),
        sa.Column("task_type", sa.String(length=50), nullable=False),
        sa.Column("zone_geohash", sa.String(length=20), nullable=True),
        sa.Column("reward_amount", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(length=20), nullable=False),
        sa.Column("assigned_partner_id", sa.Integer(), nullable=True),
        sa.Column("start_window", sa.DateTime(), nullable=False),
        sa.Column("end_window", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["incident_id"],
            ["incidents.id"],
        ),
        sa.ForeignKeyConstraint(
            ["assigned_partner_id"],
            ["partners.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Drop evidence_tasks and partners tables."""

    op.drop_table("evidence_tasks")
    op.drop_table("partners")