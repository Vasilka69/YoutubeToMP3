from proglog import ProgressBarLogger
from pytube import YouTube
from moviepy.editor import VideoFileClip

class YouTubeMP3():
    output_path_mp3 = ''
    output_path_mp4 = ''
    url = ''

    output_mp3_file = ''
    output_mp4_file = ''

    progressbardwnload = None
    progressbarconvert = None

    def SetPathAndURL(self, output_path, url):
        self.output_path_mp3 = output_path
        self.output_path_mp4 = output_path + '/mp4'
        self.url = url

    def DownloadAndConvert(self):
        if self.output_path_mp3 == '' or self.url == '':
            return

        try:
            self.DownloadMP4Audio()
        except Exception as e:
            raise ValueError(e)
        print()
        try:
            self.ConvertToMP3()
        except Exception as e:
            raise RuntimeError(e)

        self.output_path_mp3 = ''
        self.output_path_mp4 = ''
        self.url = ''

    def DownloadMP4Audio(self):
        # pytube.request.default_range_size = 1024*1024*5

        yt = YouTube(self.url, on_progress_callback=self.download_progress)

        bestaudiostream = yt.streams.get_highest_resolution()  # Выбрать максимум 1080 (уже не надо)
        # bestaudiostream = yt.streams.get_audio_only(subtype='mp3')  # Выбрать максимум 1080 (уже не надо)
        # print(bestaudiostream)
        self.output_mp4_file = bestaudiostream.download(output_path=self.output_path_mp4)
        split = self.output_mp4_file.split('\\')
        self.output_mp4_file = self.output_path_mp3 + '/mp4/' + split[len(split) - 1]
        self.output_mp3_file = self.output_path_mp3 + '\\' + split[len(split) - 1].split('.')[0] + '.mp3'
        self.progressbardwnload['value'] = 100

    def ConvertToMP3(self):
        videoclip = VideoFileClip(self.output_mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(self.output_mp3_file, logger=self.ConvertationProgressLogger(self.progressbarconvert), bitrate='3000k')
        audioclip.close()
        videoclip.close()
        self.progressbarconvert['value'] = 100

    def download_progress(self, chunk, fh, bytes_remaining):
        print('download_progress callback')
        filesize = chunk.filesize
        self.progressbardwnload['value'] = int(100 * ((filesize - bytes_remaining) / filesize))

    class ConvertationProgressLogger(ProgressBarLogger):
        def __init__(self, progressbarconvert):
            super().__init__()
            self.progressbarconvert = progressbarconvert

        def bars_callback(self, bar, attr, value, old_value=None):
            # print('convert_progress callback')
            self.progressbarconvert['value'] = int((value / self.bars[bar]['total']) * 100)

    # def DownloadAndSaveToMP3(self, progressbar):  # Не используется
    #     if self.output_path_mp3 == '' or self.url == '':
    #         return
    #
    #     self.progressbardwnload = progressbar
    #
    #     # yt = YouTube(self.url, on_progress_callback=self.on_progress)
    #     yt = YouTube(self.url)
    #     #bestaudiostream = yt.streams.get_highest_resolution() # Выбрать максимум 1080
    #     bestaudiostream = yt.streams.get_audio_only()
    #     print(bestaudiostream)
    #     self.output_mp4_file = bestaudiostream.download(output_path=self.output_path_mp3)
    #     print(self.output_mp4_file)
    #     print(self.output_mp4_file.split('.'))
    #     temp = self.output_mp4_file.split('.')
    #     newpath = ''
    #     for i in range(0, len(temp) - 1):
    #         newpath += temp[i] + '.'
    #     newpath += 'mp3'
    #     print(newpath)
    #     os.rename(self.output_mp4_file, newpath)
    #
    #     self.output_path_mp3 = ''
    #     self.output_path_mp4 = ''
    #     self.url = ''