import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

client_key = os.getenv("CLIENT_ID")
client_secret_key = os.getenv("CLIENT_SECRET_KEY")
redirect_url = os.getenv("REDIRECT_URL")


client_credentials_manager = SpotifyClientCredentials(client_id=client_key, client_secret=client_secret_key)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_playlist_tracks(playlist_id, total_tracks=500):
    """Extract tracks from the specified playlist up to a total of 500."""
    tracks = []
    limit = 100 

    for offset in range(0, total_tracks, limit):
        results = sp.playlist_tracks(playlist_id, limit=limit, offset=offset)
        tracks.extend(results['items'])

        if len(results['items']) < limit:
            break

    return tracks


def create_album_dataframe(tracks):
    """Create a DataFrame with track details."""
    
    album_data = []


    for item in tracks:
        track = item['track']
        album_info = {
            'album_id': track['album']['id'],
            'album_name': track['album']['name'],
            'release_date': track['album']['release_date'],
            'album_total_tracks': track['album']['total_tracks'],
            'album_url': track['album']['images'][0]['url']
            # 'artist_name': ', '.join(artist['name'] for artist in track['artists']),  # Join all artists' names
            # 'duration_ms': track['duration_ms'],
            # 'popularity': track['popularity']
        }
        album_data.append(album_info)


    df = pd.DataFrame(album_data)
    return df



def create_artist_dataframe(tracks):
    """Create a DataFrame with unique artist details."""
    artist_data = []
    seen_artist_ids = set()

    for item in tracks:
        track = item['track']
        for artist in track['artists']:
            if artist['id'] not in seen_artist_ids:
                artist_info = {
                    'artist_id': artist['id'],
                    'artist_name': artist['name'],
                    'external_url': artist['external_urls']['spotify'] 
                }
                artist_data.append(artist_info)
                seen_artist_ids.add(artist['id'])  


    df = pd.DataFrame(artist_data)
    return df


def create_song_dataframe(tracks):
    """Create a DataFrame with unique artist details."""
    song_data = []

    for item in tracks:
        track = item['track']
        song_info = {
            'song_id': track['id'],
            'song_name': track['name'],
            'song_duration (ms)': track['duration_ms'],
            'song_poplarity': track['popularity'],
            'date_added': item['added_at'],
            'artist_id': track['album']['artists'][0]['id'],
            'album_id': track['album']['id'],
            'song_url': track['external_urls']['spotify']
        }

        song_data.append(song_info)

    df = pd.DataFrame(song_data)
    return df



if __name__ == "__main__":
    playlist_uri = 'spotify:playlist:1RTENWq73MEx1Pop40ZZ5S'
    tracks = get_playlist_tracks(playlist_uri, total_tracks=500)
    # print(tracks[0])
    album_df = create_album_dataframe(tracks)
    print(album_df)
    # artist_df = create_artist_dataframe(tracks)
    # song_df = create_song_dataframe(tracks)


    # print(song_df)
    # song_df.to_csv('spotify_top_500_songs.csv', index=False)
    # artist_df.to_csv('spotify_top_500_artists.csv', index=False)
    # album_df.to_csv('spotify_top_500_album.csv', index=False)




# import json
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# from spotipy.oauth2 import SpotifyClientCredentials
# import os
# from datetime import datetime
# import boto3



# def lambda_handler(event, context):
#     client_key = os.getenv("CLIENT_ID")
#     client_secret_key = os.getenv("CLIENT_SECRET_KEY")
#     redirect_url = os.getenv("REDIRECT_URL")
    
#     client_credentials_manager = SpotifyClientCredentials(client_id=client_key, client_secret=client_secret_key)
#     sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
#     tracks = []
#     limit = 100
#     total_tracks = 500
#     playlist_url = 'spotify:playlist:1RTENWq73MEx1Pop40ZZ5S'

#     for offset in range(0, total_tracks, limit):
#         results = sp.playlist_tracks(playlist_url, limit=limit, offset=offset)
#         tracks.extend(results['items'])

#         if len(results['items']) < limit:
#             break

#     client = boto3.client('s3')
#     filename = "spotify_raw_"+ str(datetime.now()) +'.json'
    
#     client.put.Object(
#         Bucket = 'spotify-etl-project-meet',
#         Key = 'raw_data/to_be_processed/'+filename,
#         Body = json.dumps(tracks)
#     )