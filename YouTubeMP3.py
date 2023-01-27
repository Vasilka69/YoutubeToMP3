
from pytube import YouTube
from moviepy.editor import *

class YouTubeMP3():
    output_path_mp3 = ''
    output_path_mp4 = ''
    url = ''

    output_mp3_file = ''
    output_mp4_file = ''

    def SetPathAndURL(self, output_path, url):
        self.output_path_mp3 = output_path
        self.output_path_mp4 = output_path + '/mp4'
        self.url = url

    def DownloadAndSaveToMP3(self):
        if self.output_path_mp3 == '' or self.url == '':
            return


        yt = YouTube(self.url)
        bestaudiostream = yt.streams.get_highest_resolution() # Выбрать максимум 1080
        print(bestaudiostream)
        self.output_mp4_file = bestaudiostream.download(output_path=self.output_path_mp3)

        self.output_path_mp3 = ''
        self.output_path_mp4 = ''
        self.url = ''

    def DownloadAndConvert(self):
        if self.output_path_mp3 == '' or self.url == '':
            return

        self.DownloadMP4Audio()
        self.ConvertToMP3()

        self.output_path_mp3 = ''
        self.output_path_mp4 = ''
        self.url = ''

    def DownloadMP4Audio(self):
        yt = YouTube(self.url)
        bestaudiostream = yt.streams.get_highest_resolution() # Выбрать максимум 1080
        print(bestaudiostream)
        self.output_mp4_file = bestaudiostream.download(output_path=self.output_path_mp4)
        split = self.output_mp4_file.split('\\')
        self.output_mp4_file = self.output_path_mp3 + '/mp4/' + split[len(split) - 1]
        self.output_mp3_file = self.output_path_mp3 + '/' + split[len(split) - 1].split('.')[0] + '.mp3'


    def ConvertToMP3(self):
        videoclip = VideoFileClip(self.output_mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(self.output_mp3_file)
        audioclip.close()
        videoclip.close()
