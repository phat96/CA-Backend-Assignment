"""add tables

Revision ID: cb3c80b3f07a
Revises: bc9344f0b7e6
Create Date: 2022-12-26 13:25:11.453028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb3c80b3f07a'
down_revision = 'bc9344f0b7e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_name', sa.String(), nullable=True),
    sa.Column('salary', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.String(), nullable=True),
    sa.Column('math', sa.Integer(), nullable=False),
    sa.Column('physics', sa.Integer(), nullable=False),
    sa.Column('chemistry', sa.Integer(), nullable=False),
    sa.Column('biology', sa.Integer(), nullable=False),
    sa.Column('literature', sa.Integer(), nullable=False),
    sa.Column('history', sa.Integer(), nullable=False),
    sa.Column('philosophy', sa.Integer(), nullable=False),
    sa.Column('art', sa.Integer(), nullable=False),
    sa.Column('foreign_lang', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('job')
    # ### end Alembic commands ###
