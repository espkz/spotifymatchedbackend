import os

from playlistMaker import playlistmaker

def main():
    pm = playlistmaker(auth, id)
    os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
    os.getenv("SPOTIFY_USER_ID")

    # get last played tracks
    num_tracks = 20
    top_tracks = pm.get_top_tracks(num_tracks)


    # get playlist name from user and create playlist
    playlist = pm.create_playlist("Test")

    # populate playlist with recommended tracks
    pm.populate_playlist(playlist, top_tracks)


if __name__ == "__main__":
    main()
