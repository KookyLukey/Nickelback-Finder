"""Lyrics table

Revision ID: 2f55fbe80e32
Revises: 
Create Date: 2019-06-17 16:09:45.964453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f55fbe80e32'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lyrics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_name', sa.String(length=128), nullable=True),
    sa.Column('album', sa.String(length=128), nullable=True),
    sa.Column('lyrics', sa.String(length=128000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lyrics_album'), 'lyrics', ['album'], unique=False)
    op.create_index(op.f('ix_lyrics_lyrics'), 'lyrics', ['lyrics'], unique=False)
    op.create_index(op.f('ix_lyrics_song_name'), 'lyrics', ['song_name'], unique=True)
    op.drop_table('sqlite_sequence')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    op.drop_index(op.f('ix_lyrics_song_name'), table_name='lyrics')
    op.drop_index(op.f('ix_lyrics_lyrics'), table_name='lyrics')
    op.drop_index(op.f('ix_lyrics_album'), table_name='lyrics')
    op.drop_table('lyrics')
    # ### end Alembic commands ###
