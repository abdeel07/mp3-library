from unittest.mock import patch
from flask import Flask
from setup.controllers import UserAuth, MusicControls, PlaylistControls
from setup.models import User, db, Music, Playlist, association_table
from unittest import TestCase, mock

class TestUserAuth(TestCase):
    def setUp(self):
        # Set up a Flask test client as context
        self.app = Flask(__name__)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    @patch('setup.models.User.query')
    def test_register_user_existing_username(self, mock_query):
        # Mock the query to simulate existing user
        mock_user = User(username="existing_user", password="hashed_password")
        mock_query.filter_by.return_value.first.return_value = mock_user

        response, status_code = UserAuth.register_user({"username": "existing_user", "password": "password123"})
        
        # Check the results
        self.assertEqual(status_code, 400)
        self.assertIn("Username already exists!", response.json['message'])

    @patch('setup.models.db.session')
    @patch('setup.models.User.query')
    def test_register_user_success(self, mock_query, mock_session):
        # Ensure no user exists with the provided username
        mock_query.filter_by.return_value.first.return_value = None

        # Mock the session's add and commit methods
        mock_session.add.return_value = None
        mock_session.commit.return_value = None

        response, status_code = UserAuth.register_user({"username": "new_user", "password": "password123"})

        # Check the results
        self.assertEqual(status_code, 201)
        self.assertIn("New user registered!", response.json['message'])


class TestMusicControls(TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.user = User(id=1, username="test_user", password="hashed_password")

    def tearDown(self):
        self.app_context.pop()

    @patch('setup.models.User.query')
    @patch('setup.models.db.session')
    def test_add_riff_success(self, mock_session, mock_user_query):
        mock_user_query.filter_by.return_value.first.return_value = self.user
        fake_image_file = mock.MagicMock()
        fake_image_file.read.return_value = b'test_image_data'
        fake_mp3_file = mock.MagicMock()
        fake_mp3_file.read.return_value = b'test_mp3_data'
        data = {"user_id": 1, "title": "New Track", "artist": "New Artist"}
        files = {"image": fake_image_file, "mp3_file": fake_mp3_file}

        response = MusicControls.addRiff(data, files)
        
        self.assertEqual(response[1], 201)  # Status code for success
        self.assertIn("New Riff created!", response[0].json['message'])

        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()
        
class TestPlaylistControls(TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.user = User(id=1, username="test_user", password="hashed_password")

    def tearDown(self):
        self.app_context.pop()


    @patch('setup.models.Playlist.query')
    @patch('setup.models.User.query')
    def test_find_single_user_playlist_success(self, mock_user_query, mock_playlist_query):
        mock_user_query.get.return_value = self.user
        mock_playlist = Playlist(id=1, name="My Playlist", user_id=self.user.id)
        mock_playlist_query.filter_by.return_value.first.return_value = mock_playlist

        # Unpack the response and status code
        response, status_code = PlaylistControls.findSingleUserPlaylist(user_id=1, playlist_id=1)

        # Check the results using status_code directly
        self.assertEqual(status_code, 200)
        self.assertIn("My Playlist", response.json['playlist']['name'])

    @patch('setup.models.db.session')
    @patch('setup.models.Playlist.query')
    @patch('setup.models.Music.query')
    def test_add_to_playlist_success(self, mock_music_query, mock_playlist_query, mock_session):
        mock_playlist = Playlist(id=1, name="My Playlist", user_id=self.user.id, musics=[])
        mock_playlist_query.get_or_404.return_value = mock_playlist
        mock_music = Music(id=1, title="New Song", artist="Artist", user_id=self.user.id)
        mock_music_query.get_or_404.return_value = mock_music

        # Unpack the response and status code
        response, status_code = PlaylistControls.addToPlaylist(playlist_id=1, music_id=1)

        # Check the results using status_code directly
        self.assertEqual(status_code, 200)
        self.assertIn("Music added to playlist My Playlist successfully", response.json['message'])
        self.assertIn(mock_music, mock_playlist.musics)
        mock_session.commit.assert_called_once()

