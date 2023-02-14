import json
import requests

from track import Track
from playlist import Playlist

class playlistmaker:

    def __init__(self, authorizationToken, user_id_auth):
        """
        :param authorization_token (str): Spotify API token
        :param user_id (str): Spotify user id
        """
        self.authorizationToken = authorizationToken
        self.userAuthorization = user_id_auth

    def get_top_tracks(self, limit):
        """Get the top n tracks played by a user
        :param limit (int): Number of tracks to get. Should be <= 50
        :return tracks (list of Track): List of last played tracks
        """
        url = f"https://api.spotify.com/v1/me/top/tracks?limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        # json testing for debugging purposes
        # json_object = json.dumps(response_json)
        # with open("test.json", "w") as outfile:
        #     outfile.write(json_object)
        # f = open('test.json')
        #
        # # returns JSON object as
        # # a dictionary
        # data = json.load(f)
        #
        # # Iterating through the json
        # # list
        # for i in data['items']:
        #     print(i)
        # Closing file
        # f.close()
        tracks = [Track(track["name"], track["id"], track["artists"][0]["name"]) for track in response_json["items"]]
        return tracks


    def get_user_id(self):
        """Get the user ID of user to access their Spotify and create a playlist
        :return userid: unique string for finding user's Spotify"""
        url = f"https://api.spotify.com/v1/me"
        response = self._place_get_user_api_request(url)
        response_json = response.json()
        # json testing for debugging purposes
        # json_object = json.dumps(response_json)
        # with open("test.json", "w") as outfile:
        #     outfile.write(json_object)
        # f = open('test.json')
        userid = response_json["id"]
        return userid

    
    def create_playlist(self, name):
        """
        :param name (str): New playlist name
        :return playlist (Playlist): Newly created playlist
        """
        userid = self.get_user_id()
        data = json.dumps({
            "name": name,
            "description": "Recommended songs by Spotify Matched c:",
            "public": True
        })
        url = f"https://api.spotify.com/v1/users/31iqklcweczydwupqkc6f72t6wfq/playlists"
        response = self._place_post_api_request(url, data)
        response_json = response.json()
        playlist_id = response_json["id"]
        playlist = Playlist(name, playlist_id)
        return playlist
    

    def populate_playlist(self, playlist, tracks):
        """Add tracks to a playlist.
        :param playlist (Playlist): Playlist to which to add tracks
        :param tracks (list of Track): Tracks to be added to playlist
        :return response: API response
        """
        track_uris = [track.create_spotify_uri() for track in tracks]
        data = json.dumps(track_uris)
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
        response = self._place_post_api_request(url, data)
        response_json = response.json()
        return response_json

    def _place_get_user_api_request(self, url):
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.userAuthorization}"
            }
        )
        return response

    def _place_get_api_request(self, url):
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.authorizationToken}"
            }
        )
        return response
    
    def _place_post_api_request(self, url, data):
        response = requests.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.authorizationToken}"
            }
        )
        return response
    
    """def get_track_recommendations(self, seed_tracks, limit=50):
        Get a list of recommended tracks starting from a number of seed tracks.
        :param seed_tracks (list of Track): Reference tracks to get recommendations. Should be 5 or less.
        :param limit (int): Number of recommended tracks to be returned
        :return tracks (list of Track): List of recommended tracks
        seed_tracks_url = ""
        for seed_track in seed_tracks:
            seed_tracks_url += seed_track.id + ","
        seed_tracks_url = seed_tracks_url[:-1]
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}"
        response = self._place_get_api_request(url)
        response_json = response.json()
        tracks = [Track(track["name"], track["id"], track["artists"][0]["name"]) for
                  track in response_json["tracks"]]
        return tracks
    """
