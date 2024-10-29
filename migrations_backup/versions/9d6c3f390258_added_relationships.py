"""added relationships

Revision ID: 9d6c3f390258
Revises: 
Create Date: 2024-10-29 13:43:41.039463

"""
from alembic import op
import sqlalchemy as sa  # Ensure this import is present

# revision identifiers, used by Alembic.
revision = '9d6c3f390258'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create pizzas table
    op.create_table('pizzas',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('ingredients', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Create restaurants table
    op.create_table('restaurants',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('address', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Create restaurant_pizzas table with foreign keys
    op.create_table('restaurant_pizzas',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('price', sa.Integer(), nullable=False),
        sa.Column('restaurant_id', sa.Integer(), sa.ForeignKey('restaurants.id'), nullable=False),
        sa.Column('pizza_id', sa.Integer(), sa.ForeignKey('pizzas.id'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    # Drop the tables in reverse order
    op.drop_table('restaurant_pizzas')
    op.drop_table('restaurants')
    op.drop_table('pizzas')
