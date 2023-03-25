import threading
import time
import tkinter

import YouTubeMP3

from tkinter import *
from tkinter.ttk import Progressbar

import sys
import os

class App():
    output_path = ''
    url = ''

    output_log = ''

    def __init__(self, ytmp3: YouTubeMP3.YouTubeMP3):
        self.ytmp3 = ytmp3

        self.window = Tk()
        self.window.title('YouTubeToMP3')
        self.window.iconphoto(True, tkinter.PhotoImage(file='img/youtube.png'))

        # Вывод для moviepy
        self.output_log = open("output_log.txt", "wt")
        sys.stdout = self.output_log
        sys.stderr = self.output_log

        # Окно
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        width=500
        height=400
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        self.window.resizable(height=False, width=False)

        # Заполнение
        self.framepath = Frame(self.window)
        self.framepath.pack(fill=X, pady=45)

        self.labelpath = Label(self.framepath, text='Path to save', font=('Consolas', 14))
        self.labelpath.pack(padx=70)

        self.entrypath = Entry(self.framepath, font=('Consolas', 10))
        self.entrypath.pack(ipadx=100)

        try:
            file = open('path.txt', 'r')
            self.entrypath.insert(0,file.read())
            file.close()
        except:
            print('Файл path.txt не найден')



        self.frameurl = Frame(self.window)
        self.frameurl.pack(fill=X)

        self.labelurl = Label(self.frameurl, text='URL', font=('Consolas', 14))
        self.labelurl.pack(padx=70)
        #  textvariable
        self.entryurl = Entry(self.frameurl, font=('Consolas', 10))
        self.entryurl.pack(ipadx=100)
        # self.entryurl.insert(0, 'https://www.youtube.com/watch?v=o4nfgcI1qk8')

        self.framedwnload = Frame(self.window)
        self.framedwnload.pack(fill=X, pady=20)

        self.labeldwnload = Label(self.framedwnload, text='Downloading', font=('Consolas', 14))
        self.labeldwnload.pack(padx=70)

        self.progressbardwnload = Progressbar(self.framedwnload, length=100, mode='determinate')
        self.progressbardwnload.pack(ipadx=30)


        self.frameconvert = Frame(self.window)
        self.frameconvert.pack(fill=X)

        self.labelconvert = Label(self.frameconvert, text='Converting', font=('Consolas', 14))
        self.labelconvert.pack(padx=70)

        self.progressbarconvert = Progressbar(self.frameconvert, length=100, mode='determinate')
        self.progressbarconvert.pack(ipadx=30)

        self.startbtn = Button(self.frameconvert, text='Start', font=('Consolas', 14), command=self.Threading)
        self.startbtn.pack(pady=20, padx=width/4)

        self.window.bind_all('<Key>', self._onKeyRelease, '+')
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def Threading(self):
        thread = threading.Thread(target=self.Start)
        thread.start()

    def Start(self):
        self.progressbardwnload['value'] = 0
        self.progressbarconvert['value'] = 0
        output_path = self.entrypath.get()
        try:
            file = open('path.txt', 'w')
            file.write(output_path)
            file.close()
        except:
            print('Какой то трабл с записью файла =)')

        url = self.entryurl.get()
        self.ytmp3.SetPathAndURL(output_path, url)

        def process():
            self.ytmp3.DownloadAndConvert(self.progressbardwnload, self.progressbarconvert)
            self.progressbardwnload['value'] = 100
            self.progressbarconvert['value'] = 100
            print('Прошло проехало')
        thread = threading.Thread(target=process)
        print('Пошло поехало')
        thread.start()

        os.startfile(output_path)


    def _onKeyRelease(self, event):
        ctrl = (event.state & 0x4) != 0
        if event.keycode == 88 and ctrl and event.keysym.lower() != "x":
            event.widget.event_generate("<<Cut>>")

        if event.keycode == 86 and ctrl and event.keysym.lower() != "v":
            event.widget.event_generate("<<Paste>>")

        if event.keycode == 67 and ctrl and event.keysym.lower() != "c":
            event.widget.event_generate("<<Copy>>")


    def on_closing(self):
        self.output_log.close()
        self.window.destroy()


