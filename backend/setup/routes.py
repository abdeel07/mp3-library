from flask import request, jsonify, Blueprint
from .models import db, User, Playlist, Music
from .controllers import UserAuth, MusicControls, PlaylistControls
import base64

# App Routes Decorator
app_routes = Blueprint('app_routes', __name__)

# Auth endpoints
@app_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json();
    response, status_code = UserAuth.register_user(data)
    return response, status_code
    

@app_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return UserAuth.login_user(data)


@app_routes.route('/logout', methods=['DELETE'])
def logout():
    return UserAuth.logout()



# User endpoints
@app_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username})
    else:
        return jsonify({'message': 'User not found'}), 404

@app_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user:
        data = request.get_json()
        user.username = data['username']
        db.session.commit()
        return jsonify({'message': 'User updated!'})
    else:
        return jsonify({'message': 'User not found'}), 404

@app_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted!'})
    else:
        return jsonify({'message': 'User not found'}), 404


@app_routes.route('/user/<int:user_id>/music', methods=['GET'])
def get_user_music(user_id):

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    user_music = Music.query.filter_by(user_id=user_id).all()
    if not user_music:
        return jsonify({'message': 'No music found for this user'}), 404
    print(user_music)
    music_list = []
    for music in user_music:
        music_data = {
            'id':music.id,
            'title': music.title,
            'artist': music.artist,
            'image': base64.b64encode(music.image).decode('utf-8') if music.image else None,
            'mp3_file': base64.b64encode(music.mp3_file).decode('utf-8') if music.mp3_file else None,
            'like':music.like
        }
        music_list.append(music_data)

    return jsonify({'music': music_list}), 200

@app_routes.route('/user/<int:user_id>/favorites', methods=['GET'])
def get_user_music_favorites(user_id):

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    user_music = Music.query.filter_by(user_id=user_id).all()
    if not user_music:
        return jsonify({'message': 'No music found for this user'}), 404
    print(user_music)
    music_list = []
    for music in user_music:
        if music.like:
            music_data = {
                'id':music.id,
                'title': music.title,
                'artist': music.artist,
                'image': base64.b64encode(music.image).decode('utf-8') if music.image else None,
                'mp3_file': base64.b64encode(music.mp3_file).decode('utf-8') if music.mp3_file else None,
                'like':music.like
            }

            music_list.append(music_data)

    return jsonify({'music': music_list}), 200

@app_routes.route('/user/<int:user_id>/playlists', methods=['GET'])
def get_user_playlist(user_id):

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    user_playlists = Playlist.query.filter_by(user_id=user_id).all()
    if not user_playlists:
        return jsonify({'message': 'No music found for this user'}), 404
    print(user_playlists)
    playlists = []
    for playlist in user_playlists:
        playlist_data = {
            'id':playlist.id,
            'name': playlist.name,
            'image': base64.b64encode(playlist.image).decode('utf-8') if playlist.image else None,
        }
        playlists.append(playlist_data)

    return jsonify({'playlists': playlists}), 200

@app_routes.route('/playlists/<int:user_id>/<int:playlist_id>', methods=['GET'])
def findSingleUserPlaylist(user_id, playlist_id):
    return PlaylistControls.findSingleUserPlaylist(user_id, playlist_id)


# Music endpoints
@app_routes.route('/music', methods=['POST'])
def create_music():
    # return  MusicControls.addRiff(request.form)
    # Access standard form data
    return MusicControls.addRiff(request.form, request.files) 



@app_routes.route('/music/<int:music_id>/add_fav', methods=['POST'])
def add_to_fav(music_id):
    music = Music.query.get(music_id)

    music.like = True
    
    db.session.commit()
    
    return jsonify({'message': 'Music added to favorits successfully'})

@app_routes.route('/music/<int:music_id>/remove_fav', methods=['POST'])
def remove_from_fav(music_id):
    music = Music.query.get(music_id)

    music.like = False
    
    db.session.commit()
    
    return jsonify({'message': 'Music removed from favorits successfully'})

# Playlist endpoints
@app_routes.route('/playlist', methods=['POST'])
def create_playlist():
    
    return PlaylistControls.addPlaylist(request.form, request.files);

@app_routes.route('/playlist/<int:playlist_id>/<int:music_id>', methods=['POST'])
def addToPlaylist(playlist_id, music_id):
    
    return PlaylistControls.addToPlaylist(playlist_id, music_id)
    
def get_music_by_playlist_id(playlist_id):
    playlist = Playlist.query.get(playlist_id)
    if playlist:
        return playlist.musics
    else:
        return []
    
@app_routes.route('/playlist/<int:playlist_id>/music', methods=['GET'])
def get_music_by_playlist(playlist_id):
    music = get_music_by_playlist_id(playlist_id)
   
    # Create a list of music data for the playlist
    music_list = [{
        'id':track.id,
        'title': track.title,
        'artist': track.artist,
        'image': base64.b64encode(track.image).decode('utf-8') if track.image else None,
        'mp3_file': base64.b64encode(track.mp3_file).decode('utf-8') if track.mp3_file else None,
        'like':track.like
        # Add more attributes as needed
    } for track in music]

    return jsonify({"playlistMusic": music_list }), 200

@app_routes.route('/playlist/<int:playlist_id>', methods=['DELETE'])
def remove_playlist(playlist_id):
    # Attempt to retrieve the playlist from the database
    playlist = Playlist.query.get(playlist_id)

    # Check if the playlist exists
    if playlist:
        # Delete the playlist from the database
        db.session.delete(playlist)
        db.session.commit()
        return jsonify({'message': 'Playlist deleted successfully'}), 200
    else:
        # Return an error message if the playlist does not exist
        return jsonify({'error': 'Playlist not found'}), 404

@app_routes.route('/music/<int:music_id>', methods=['DELETE'])
def remove_music(music_id):
    # Attempt to retrieve the music track from the database
    music = Music.query.get(music_id)

    # Check if the music track exists
    if music:
        # Delete the music track from the database
        db.session.delete(music)
        db.session.commit()
        return jsonify({'message': 'Music track deleted successfully'}), 200
    else:
        # Return an error message if the music track does not exist
        return jsonify({'error': 'Music track not found'}), 404
    
@app_routes.route('/playlist/<int:playlist_id>/<int:music_id>', methods=['DELETE'])
def remove_music_from_playlist(playlist_id, music_id):
    
    return PlaylistControls.removeSongFromPlaylist(playlist_id, music_id);
