import App
import YouTubeMP3


def main():
    ytmp3 = YouTubeMP3.YouTubeMP3()
    app = App.App(ytmp3)

    #ytmp3.DownloadAndConvert()


if __name__ == '__main__':
    main()