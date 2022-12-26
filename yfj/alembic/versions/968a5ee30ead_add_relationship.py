"""add relationship

Revision ID: 968a5ee30ead
Revises: 6cd833e6dc33
Create Date: 2022-12-26 16:33:01.254639

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '968a5ee30ead'
down_revision = '6cd833e6dc33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    # ### end Alembic commands ###
