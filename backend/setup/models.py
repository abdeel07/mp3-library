from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import LargeBinary, Table, Column, Integer, ForeignKey
from passlib.hash import pbkdf2_sha256 as sha256

db = SQLAlchemy()

# Create 'Association' Table
association_table = Table('association', db.Model.metadata,
    Column('playlist_id', Integer, ForeignKey('playlists.id')),
    Column('music_id', Integer, ForeignKey('musics.id'))
)

# Create 'Users' Table
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
    
# Create 'Music' Table
class Music(db.Model):
    __tablename__ = "musics"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    image = db.Column(LargeBinary, nullable=True)
    mp3_file = db.Column(LargeBinary, nullable=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('musics', lazy=True))
    like = db.Column(db.Boolean,nullable=True)
    playlists = db.relationship('Playlist', secondary=association_table, back_populates='musics')

# Create 'Playlists" Table
class Playlist(db.Model):
    __tablename__ = "playlists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(LargeBinary, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('playlists', lazy=True))
    musics = db.relationship('Music', secondary=association_table, back_populates='playlists')
    likes = db.Column(db.Integer, default=0, nullable=False)
    
    def increment_likes(self):
        self.likes += 1

    def decrement_likes(self):
        self.likes -= 1