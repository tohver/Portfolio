import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
from typing import Any


def process_song_file(cur: Any, filepath: str) -> None:
    """
    Takes the database cursor and the path to the song JSON files.
    Extracts the data, transforms them and populats the tables. 
    @param cur: the database cursor
    @param filepath: the path to the song files
    """
    # open song file
    df = df = pd.read_json(filepath, lines = True)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur: Any, filepath: str) -> None:
    """    
    Takes the database cursor and the path to the log JSON files.
    Extracts the data, transforms them and populats the tables. 
    @param cur: the database cursor
    @param filepath: the path to the song files
    """

    # open log file
    df = pd.read_json(filepath, lines = True)

    # filter by NextSong action
    df = df[df.page == "NextSong"]

    # convert timestamp column to datetime
    t = pd.to_datetime(df.ts, unit = "ms")
    
    # insert time data records
    time_data = {
    "start_time" : t,
    "hour" : t.dt.hour,
    "day" : t.dt.day,
    "week" : t.dt.week,
    "month" : t.dt.month,
    "year" : t.dt.year,
    "weekday" : t.dt.weekday 
    }

    column_labels = ()
    time_df = pd.DataFrame(data = time_data)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (
            pd.to_datetime(row.ts, unit = "ms"),
            row.userId,
            row.level,
            songid,
            artistid,
            row.sessionId,
            row.location,
            row.userAgent
        )

        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur: Any, conn: Any, filepath: str, func: Any) -> None:
    """
    Processes the song and log JSON files and loads the data into tables. 
    @param conn: the database connection
    @param filepath: the path to the data directory
    @param func: the function to process the files
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath = 'data/song_data', func = process_song_file)
    process_data(cur, conn, filepath = 'data/log_data', func = process_log_file)

    conn.close()


if __name__ == "__main__":
    main()