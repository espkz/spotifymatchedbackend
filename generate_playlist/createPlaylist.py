import os

from playlistMaker import playlistmaker

def main():
    
    # Export the environment variables:
    # $ export SPOTIFY_AUTHORIZATION_TOKEN=value_grabbed_from_spotify
    # $ export SPOTIFY_USER_ID=value_grabbed_from_spotify
    # or otherwise manually put it in as variables and substitute
    # auth = ""
    # id = ""
    
    pm = playlistmaker(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"), os.getenv("SPOTIFY_USER_ID")) # auth, id
    
    # get last played tracks
    num_tracks = 20
    top_tracks = pm.get_top_tracks(num_tracks)


    # get playlist name from user and create playlist
    playlist = pm.create_playlist("Test")

    # populate playlist with recommended tracks
    pm.populate_playlist(playlist, top_tracks)


if __name__ == "__main__":
    main()
