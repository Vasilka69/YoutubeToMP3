import threading
import time

import YouTubeMP3

from tkinter import *
from tkinter.ttk import Progressbar


class App():
    output_path = ''
    url = ''


    def __init__(self, ytmp3: YouTubeMP3.YouTubeMP3):
        self.ytmp3 = ytmp3

        self.window = Tk()
        self.window.title('YouTubeToMP3')

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

        self.labelpath = Label(self.framepath, text='Path', font=('Consolas', 14))
        self.labelpath.pack(padx=70)

        self.entrypath = Entry(self.framepath, font=('Consolas', 10))
        self.entrypath.pack(ipadx=100)
        # self.entrypath.insert(0, 'C:\\Users\\Packard\\Desktop\\1.Для добавки')


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

        self.startbtn = Button(self.frameconvert, text='Start', font=('Consolas', 14), command=self.Start)
        self.startbtn.pack(pady=20, padx=width/4)

        self.window.mainloop()

    def Start(self):
        self.progressbardwnload['value'] = 0
        self.progressbarconvert['value'] = 0
        output_path = self.entrypath.get()
        url = self.entryurl.get()
        self.ytmp3.SetPathAndURL(output_path, url)

        # def temp():
        #     # self.ytmp3.DownloadAndConvert()
        #     #threading.Thread(target=self.ytmp3.DownloadAndConvert()).start()
        #     print('Пошло поехало')
        #     for i in range(100):
        #         self.progressbardwnload['value'] = i
        #         time.sleep(0.05)
        #     for i in range(100):
        #         self.progressbarconvert['value'] = i
        #         time.sleep(0.05)
        #
        # threading.Thread(target=self.ytmp3.DownloadAndConvert()).start()
        print('Пошло поехало')
        threading.Thread(target=self.ytmp3.DownloadAndConvert).start()
        print('Прошло проехало')
        self.progressbardwnload['value'] = 100
        self.progressbarconvert['value'] = 100
        # for i in range(100):
        #     self.progressbardwnload['value'] = i
        #     time.sleep(0.05)
        # for i in range(100):
        #     self.progressbarconvert['value'] = i
        #     time.sleep(0.05)
        # self.ytmp3.DownloadAndConvert()


