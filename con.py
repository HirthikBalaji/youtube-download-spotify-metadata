from pytube import YouTube, Playlist
import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TALB, TPE1, TORY
import re


def remove_punctuation(input_string):
    # Define a regular expression pattern to match punctuation and special characters
    pattern = r'[^\w\s]'  # Matches any character that is not a word character or whitespace

    # Substitute matched characters with an empty string
    clean_string = re.sub(pattern, '', input_string)
    return clean_string


def download_videos_from_playlist(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        for video in playlist.video_urls:
            Download_video_streams(video, playlist.title)
    except Exception as e:
        print(f"Error : {str(e)}")


def Download_video_streams(url, foldername="NORMAL"):
    try:
        if "http" in url:
            yt = YouTube(url)
        else:
            yt = url
        stream = yt.streams.get_highest_resolution()
        # List available streams and their URLs
        print("-" * 80)
        # print(url,"\n")
        print(yt.title, "\n")
        print(f"Resolution: {stream.resolution}\n")
        print(f"Mime Type: {stream.mime_type}\n")
        # print(f"URL: {stream.url}\n")
        if not os.path.exists(f"%userprofile%\\Downloads\\{remove_punctuation(foldername)}"):
            os.mkdir(f"%userprofile%\\Downloads\\{remove_punctuation(foldername)}")
        print("Downloading..\n")
        thumbnail = yt.thumbnail_url
        os.system(f"wget --quiet '{thumbnail}' -O Thumbnail.jpg")
        os.system(
            f"wget --quiet --show-progress '{stream.url}' -O '%userprofile%\\Downloads\\{remove_punctuation(foldername)}\\{remove_punctuation(yt.title)}.mp4'")
        os.system(
            f"ffmpeg -i '%userprofile%\\Downloads\\{remove_punctuation(foldername)}\\{remove_punctuation(yt.title)}.mp4' -c:a mp3 -b:a 640k -metadata title='{remove_punctuation(yt.title)}'  '%userprofile%\\Downloads\\{remove_punctuation(foldername)}\\{remove_punctuation(yt.title)}.mp3'")
        # Open the MP3 file
        sp = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id="REPLACE WITH YOUR CLIENT ID",
                                                                client_secret="REPLACE WITH YOUR CLIENT SECRET"))  # DON'T WORRY ITS COMPLETELY FREE NO CREDIT CARD REQUIRED...
        result = sp.search(remove_punctuation(yt.title))
        # pprint.pprint(result)

        ALBUM_NAME = result["tracks"]["items"][0]["album"]["name"]
        RELEASE_DATE = result["tracks"]["items"][0]["album"]["release_date"]
        ARTIST_NAME = result["tracks"]["items"][0]["album"]["artists"][0]["name"]

        audio = MP3(f"%userprofile%\\Downloads\\{remove_punctuation(foldername)}\\{remove_punctuation(yt.title)}.mp3",
                    ID3=ID3)

        # Add album name
        audio.tags.add(TALB(encoding=3, text=ALBUM_NAME))

        # Add artist name
        audio.tags.add(TPE1(encoding=3, text=ARTIST_NAME))
        audio.tags.add(TORY(encoding=3, text=RELEASE_DATE))

        audio.tags.add(
            APIC(
                encoding=3,  # 3 is for utf-8
                mime="image/jpeg",  # can be image/jpeg or image/png
                type=3,  # 3 is for the cover image
                desc='Cover',
                data=open("Thumbnail.jpg", mode='rb').read()
            )
        )
        audio.save()

        print()
        os.remove("Thumbnail.jpg")
        os.remove(f'%userprofile%\\Downloads\\{remove_punctuation(foldername)}\\{remove_punctuation(yt.title)}.mp4')

    except Exception as e:
        print(f"Error: {str(e)}")


def differentiate_url(url):
    if 'list' in url:
        download_videos_from_playlist(url)
    else:
        Download_video_streams(url)


# differentiate_url(youtube_url)
if __name__ == "__main__":
    youtube_url = input("URL:")
    differentiate_url(youtube_url)
