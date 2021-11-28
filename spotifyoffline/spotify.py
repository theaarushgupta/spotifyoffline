from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

def _performOAuth2(credentials: dict) -> SpotifyClientCredentials:
    apiCredentials = credentials["spotifyAPI"]
    credentialManager = SpotifyClientCredentials(
        apiCredentials["id"],
        apiCredentials["secret"]
    )
    return credentialManager

def initializeSpotify(credentials) -> Spotify:
    spotify = Spotify(client_credentials_manager = _performOAuth2(credentials))
    return spotify

def getSearchableTracks(spotify: Spotify, playlistID: str) -> list:
    searchableTracks = []
    playlist = spotify.playlist(playlistID)
    for track in playlist["tracks"]["items"]:
        track = track["track"]
        name = track["name"]
        artist = track["artists"][0]["name"]
        searchableTracks.append(f"{name} by {artist} lyrics")
    return searchableTracks