from spotifyoffline.credentials import getCredentialsFilename, fetchCredentials
from spotifyoffline.spotify import initializeSpotify, getSearchableTracks
from spotifyoffline.youtube import youtubeURLFromTrackName, downloadYoutubeVideoFromURL
from spotifyoffline.conversion import convertMP3ToMP4

from os import getcwd
from os.path import join
from shutil import rmtree

def main() -> None:
    print("[info] clearing \"music/\" directory for new downloads")
    music = join(getcwd(), "music")
    try:
        rmtree(music)
    except FileNotFoundError:
        pass
    try:
        downloaded = 0
        credentialsFilename = getCredentialsFilename()
        credentials = fetchCredentials(credentialsFilename)
        spotify = initializeSpotify(credentials)
        tracks = getSearchableTracks(spotify, credentials["playlist"])
        print("[info] starting download")
        for track in tracks:
            url = youtubeURLFromTrackName(track)
            name = track.replace(" lyrics", "")
            downloadComplete = downloadYoutubeVideoFromURL(name, url)
            filename = name.replace(" ", "-").lower() +".mp4"
            print("[info] converting file type from MP4 to MP3")
            convertMP3ToMP4(filename)
            if downloadComplete:
                downloaded += 1
    except KeyboardInterrupt:
        exit()