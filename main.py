"""
This file is purely for demonstration as to how the two other files can work together
"""
from oracle_module import oracle
from table_cls import database, new_database

def define_all_objects():
    cd = database("cd_tbl", id="cd_id",title="cd_title", release_date= "cd_release_date") #title becomes field["title"] = "cd_title"
    artist = database("artist_tbl", id="artist_id", name="artist_name")
    genre = database("genre_tbl", id="genre_id", name="genre_name", description= "genre_description")
    musician = database("musician_tbl", id="musician_id", name="musician_name")
    song = database("song_tbl", id="song_id", title="song_title")
    track = database("track_tbl", id="track_id", title="track_title", length="track_length", release="track_release_date")
    artist_track = database("artist_track_lnk", artist_id="fk_artist_id", track_id="fk_artist_id")
    cd_track = database("cd_track_lnk", cd_id="fk_cd_id", track_id="fk_track_id")
    genre_track = database("genre_track_lnk", genre_id="fk_genre_id", track_id="fk_genre_id")
    musician_artist = database("musician_artist_lnk", musician_id="fk_musician_id", artist_id="fk_artist_id")
    musician_song = database("musician_song_lnk", musician_id="fk_musician_id", song_id="fk_song_id")
    musician_track = database("musician_track_lnk", musician_id="fk_musician_id", track_id="fk_track_id")
    song_track = database("song_track_lnk", song_id="fk_song_id", track_id="fk_track_id")
    spices = database("spice_tbl", id="id", name="name", scoval="scoval")

    return [cd, artist, genre, musician, song, track, artist_track, cd_track, genre_track, musician_artist, musician_song, musician_track, song_track]

def make_new_table():
    pass

def display_all_tables(lst):
    for table in lst:
        print(f"{table.table_name} with fields {table.fields}")

def find_tbl_frm_lst(lst, looking_for):
    for table in lst:
        if table.table_name == looking_for:
            return table

def main():
    oracle_conn = oracle() ##OPENS CONNECTION
    
    lst_of_tbls = define_all_objects()
    temp = find_tbl_frm_lst(lst_of_tbls,"song_tbl")
    rec = oracle_conn.get_record(temp.table_name, temp.fields["id"], "S13")
    print(rec)

    oracle_conn.close_connection() #CLOSES THE CONNECTION

if __name__ == "__main__":
    main()