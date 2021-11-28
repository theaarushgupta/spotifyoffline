from pytube import YouTube

from requests import get
from re import findall

def youtubeURLFromTrackName(name: str) -> str:
    result = get(f"https://youtube.com/results?search_query={name}")
    result = result.text
    videoIDs = findall(r"watch\?v=(\S{11})", result)
    videoID = videoIDs[0]
    return f"https://youtube.com/watch?v={videoID}"

def downloadYoutubeVideoFromURL(name: str, url: str) -> bool:
    try:
        filename = name.replace(" ", "-").lower() +".mp4"
        YouTube(url).streams.filter(file_extension = "mp4").first().download(filename = filename, output_path = "music")
    except:
        print(f"[error] cannot download video at: \"{url}\"")
        return False
    print(f"[info] downloaded \"{name}\" as \"{filename}\"")
    return True