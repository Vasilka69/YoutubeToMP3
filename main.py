import App
import YouTubeMP3


def main():
    ytmp3 = YouTubeMP3.YouTubeMP3()
    app = App.App(ytmp3)

    #ytmp3.DownloadAndConvert()
    #ytmp3.DownloadAndSaveToMP3


if __name__ == '__main__':
    main()

# Build command
# pyinstaller --noconfirm --onedir --windowed --icon "C:/Users/Vasili4/Documents/GitHub/YoutubeToMP3/img/youtube.ico" --add-data "C:/Users/Vasili4/Documents/GitHub/YoutubeToMP3/img;img/" --add-data "C:/Users/Vasili4/Documents/GitHub/YoutubeToMP3/venv/Lib/site-packages/moviepy;moviepy/"  "C:/Users/Vasili4/Documents/GitHub/YoutubeToMP3/main.py"
# Билд в dist
