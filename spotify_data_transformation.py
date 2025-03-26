import pandas as pd
from datetime import datetime
from utils import convert_date, extract_date_components, handling_outliers_songs
from utils import extract_duration_categories, extracting_song_minutes_seconds, age_of_all_song





def transform_spotify_album():
    album_df = pd.read_csv("spotify_top_500_album.csv")
    # album_df.head()

    # Handling Duplicate records
    album_df.drop_duplicates(inplace=True)

    # Apply the conversion function to the release_date column
    album_df['release_date'] = album_df['release_date'].apply(convert_date)

    # Extract date components such as year, month, day, isweekend, etc.
    album_df = extract_date_components(album_df, 'release_date')
    
    return album_df


def transform_spotify_artist():
    artist_df = pd.read_csv('spotify_top_500_artists.csv')
    
    # Handling duplicate artists information
    artist_df.drop_duplicates(inplace=True)

    return artist_df


def trasform_spotify_song():
    song_df = pd.read_csv("spotify_top_500_songs.csv")

    # Handling duplicate songs
    song_df.drop_duplicates(inplace=True)

    # Data cleaning
    song_df.columns = song_df.columns.str.lower().str.replace(' ', '_')

    # Extracting minute and seconds from miliseconds
    song_df = extracting_song_minutes_seconds(song_df)
    

    # Extracting date component for songs
    song_df = extract_date_components(song_df, 'date_added')

    # Detecting and flagging outliers
    song_df = handling_outliers_songs(song_df)

    # Assigning length of song
    song_df = extract_duration_categories(song_df)
    
    song_df = age_of_all_song(song_df)

    return song_df