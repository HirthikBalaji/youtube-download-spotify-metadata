**Project Title: YouTube Playlist Downloader with Spotify Metadata**

**Overview:**
This Python script allows users to download videos from either individual YouTube URLs or entire playlists. It also fetches metadata from Spotify for the downloaded videos and embeds it into the downloaded MP3 files. The script utilizes popular libraries such as Pytube for YouTube video handling, Spotipy for Spotify API integration, Mutagen for audio metadata manipulation, and FFmpeg for video conversion. 

**Setup:**
1. **Python Environment:**
   - Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).
   - Recommended Python version: Python 3.x.

2. **Library Installation:**
   - Install the required libraries using pip, Python's package manager. Run the following command in your terminal or command prompt:
     ```
     pip install pytube3 spotipy mutagen
     ```

3. **FFmpeg Installation:**
   - Install FFmpeg, a multimedia framework used for handling audio and video data. You can download it from the [official FFmpeg website](https://ffmpeg.org/download.html) or install it via package managers like Homebrew (for macOS) or Chocolatey (for Windows).
   - Ensure FFmpeg is added to your system's PATH environment variable.

4. **Spotify API Credentials:**
   - Obtain Spotify API credentials (Client ID and Client Secret) by creating a Spotify Developer account and registering your application. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) to create a new application.
   - Replace `"REPLACE WITH YOUR CLIENT ID"` and `"REPLACE WITH YOUR CLIENT SECRET"` in the script with your actual credentials.

**Usage:**
1. **Run the Script:**
   - Open your terminal or command prompt and navigate to the directory containing the script.
   - Run the script using the command:
     ```
     python main.py
     ```

2. **Input YouTube URL:**
   - Upon running the script, you'll be prompted to input a YouTube URL.
   - You can input either a single video URL or a playlist URL. The script automatically detects and handles playlists.

3. **Download Progress:**
   - The script will display information about the video being downloaded, including its title, resolution, and MIME type.
   - Progress updates will be shown during the download process.

4. **Spotify Metadata Embedding:**
   - After downloading the video, the script fetches metadata from Spotify based on the video's title.
   - Metadata such as album name, artist name, and release date are retrieved and embedded into the downloaded MP3 file.

**Additional Notes:**
- **Folder Structure:**
  - The downloaded files are saved in the `Downloads` directory of the user's profile.
  - If downloading from a playlist, each video is saved in a subdirectory named after the playlist.
  - Ensure the script has necessary permissions to create directories and write files in the specified location.

- **Error Handling:**
  - The script includes error handling mechanisms to catch and display any exceptions that may occur during execution.
  - If an error occurs, the script prints an error message along with details of the exception.

**Disclaimer:**
- This script is provided as-is and should be used responsibly and in compliance with YouTube's and Spotify's terms of service.
- Use of the Spotify API is subject to Spotify's Developer Terms of Service, available on the Spotify Developer website.

**Author:**
- Hirthik Balaji C

**License:**
- GNU General Public License

**Feedback and Contributions:**
- Feedback and contributions to improve the script are welcome. Feel free to submit pull requests or open issues on the project's GitHub repository, if available.

**Acknowledgements:**
- Acknowledge any third-party libraries, APIs, or resources used in the script.
