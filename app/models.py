from app import db

class Lyrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_name = db.Column(db.String(128), index=True, unique=True)
    album = db.Column(db.String(128), index=True)
    lyrics = db.Column(db.String(128000), index=True)

    def __repr__(self):
        return '<Song {}>'.format(self.song_name)
