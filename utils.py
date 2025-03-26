import pandas as pd
from datetime import datetime


def convert_date(date_str):
    # Check if the date string is just a year (length 4 and all digits)
    if len(date_str) == 4 and date_str.isdigit():
        return pd.to_datetime(date_str + '-01-01')  # Append '-01-01' to the year
    else:
        # Try converting the full date; if it fails, return NaT
        try:
            return pd.to_datetime(date_str, format='%Y-%m-%d', errors='coerce')
        except ValueError:
            return pd.NaT



def extract_date_components(df, date_column):
    """
    Enhances a DataFrame by adding new columns based on the date information from the specified date_column.
    
    Parameters:
        df (pd.DataFrame): The DataFrame containing the date column.
        date_column (str): The name of the column in df that contains date information.
    
    Returns:
        pd.DataFrame: The original DataFrame with added columns for year, month, day, is_weekend, and day_of_week.
    """
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
    # df[date_column] = df[date_column].dt.strftime('%Y-%d-%m')
    
    df['year'] = df[date_column].dt.year
    df['month'] = df[date_column].dt.month
    df['day'] = df[date_column].dt.day
    df['is_weekend'] = df[date_column].dt.dayofweek > 4
    df['day_of_week_numeric'] = df[date_column].dt.dayofweek
    df['day_of_week_name'] = df[date_column].dt.day_name()
    
    return df



def handling_outliers_songs(song_df):
    Q1 = song_df['total_seconds'].quantile(0.25)
    Q3 = song_df['total_seconds'].quantile(0.75)
    IQR = Q3 - Q1

    # Define bounds for outliers
    lower_bound = Q1 - 2.5 * IQR
    upper_bound = Q3 + 2.5 * IQR

    # Identify outliers
    song_df['is_outlier'] = (song_df['total_seconds'] < lower_bound) | (song_df['total_seconds'] > upper_bound)

    return song_df

def extract_duration_categories(song_df):
    song_df['duration_category'] = pd.cut(song_df['total_seconds'],
                                    bins=[0, 180, 300, 500],
                                    labels=['short', 'medium', 'long'],
                                    right=False)
    
    return song_df
    

def extracting_song_minutes_seconds(song_df):
    song_df['duration_minutes'] = round(song_df['song_duration_(ms)'] / 60000)
    song_df['duration_seconds'] = round((song_df['song_duration_(ms)'] % 60000) / 1000, 0)
    song_df['total_seconds'] = song_df['duration_minutes'] * 60 + song_df['duration_seconds']

    return song_df


def age_of_all_song(song_df):
    song_df['date_added'] = pd.to_datetime(song_df['date_added']).dt.tz_localize(None)  # Making it timezone-naive
 
    # Calculate the current date as timezone-naive
    current_date = datetime.now().replace(tzinfo=None)

    song_df['age_of_song_days'] = (current_date - song_df['date_added']).dt.days

    return song_df