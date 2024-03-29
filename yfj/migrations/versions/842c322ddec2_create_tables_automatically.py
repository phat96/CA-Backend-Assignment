"""create tables automatically

Revision ID: 842c322ddec2
Revises:
Create Date: 2022-12-28 10:46:39.402922

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '842c322ddec2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'job',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('job_name', sa.String(), nullable=True),
        sa.Column('salary', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'student',
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
        sa.Column('average_score', sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'student_job',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('job_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['job_id'], ['job.id']),
        sa.ForeignKeyConstraint(['student_id'], ['student.id']),
        sa.PrimaryKeyConstraint('student_id', 'job_id'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_job')
    op.drop_table('student')
    op.drop_table('job')
    # ### end Alembic commands ###
