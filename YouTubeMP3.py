from pytube import YouTube
from moviepy.editor import *

import os

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

    def DownloadAndSaveToMP3(self, progressbar):
        if self.output_path_mp3 == '' or self.url == '':
            return

        self.progressbar = progressbar

        # yt = YouTube(self.url, on_progress_callback=self.on_progress)
        yt = YouTube(self.url)
        #bestaudiostream = yt.streams.get_highest_resolution() # Выбрать максимум 1080
        bestaudiostream = yt.streams.get_audio_only()
        print(bestaudiostream)
        self.output_mp4_file = bestaudiostream.download(output_path=self.output_path_mp3)
        print(self.output_mp4_file)
        print(self.output_mp4_file.split('.'))
        temp = self.output_mp4_file.split('.')
        newpath = ''
        for i in range(0, len(temp) - 1):
            newpath += temp[i] + '.'
        newpath += 'mp3'
        print(newpath)
        os.rename(self.output_mp4_file, newpath)

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

    def on_progress(self, stream, chunk, bytes_remaining):
        self.progressbar['value'] = bytes_remaining/len(stream)

    def DownloadMP4Audio(self):
        yt = YouTube(self.url)
        bestaudiostream = yt.streams.get_highest_resolution() # Выбрать максимум 1080
        print(bestaudiostream)
        self.output_mp4_file = bestaudiostream.download(output_path=self.output_path_mp4)
        split = self.output_mp4_file.split('\\')
        self.output_mp4_file = self.output_path_mp3 + '/mp4/' + split[len(split) - 1]
        self.output_mp3_file = self.output_path_mp3 + '\\' + split[len(split) - 1].split('.')[0] + '.mp3'


    def ConvertToMP3(self):
        videoclip = VideoFileClip(self.output_mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(self.output_mp3_file)
        audioclip.close()
        videoclip.close()
