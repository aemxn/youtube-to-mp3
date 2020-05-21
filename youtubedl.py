#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Apr 02, 2019 10:38:13 PM CST  platform: Windows NT

import sys
import subprocess

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from tkinter import messagebox
import youtubedl_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    youtubedl_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    youtubedl_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    # v0.1 - using youtube-dl to download single video as mp3 track
    def start_YoutubeDL(self):
        url = self.entry_single_video_url.get()
        command = "cmd.exe /K youtube-dl.exe --extract-audio --output \"%(title)s.%(ext)s\" --audio-format mp3 --audio-quality 0 " + url
        if url:
            start = messagebox.askyesno("Info", "You are about to download " + url)
            if start:
                subprocess.Popen(command)
                # TODO v0.2
                # self.entry_single_video_url.configure(state=tk.DISABLED)
                # self.entry_single_video_url.configure(background="grey")
                # - disable text field while progress is running
                # - reenable text field when progress is finished
        else:
            messagebox.showinfo("Info", "URL field cannot be empty")

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x175+883+309")
        top.title("Youtube to MP3 Downloader")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.017, rely=0.057, relheight=0.829
                , relwidth=0.958)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=575)

        self.entry_single_video_url = tk.Entry(self.Frame1)
        self.entry_single_video_url.place(relx=0.035, rely=0.414, height=30
                , relwidth=0.929)
        self.entry_single_video_url.configure(background="white")
        self.entry_single_video_url.configure(disabledforeground="#a3a3a3")
        self.entry_single_video_url.configure(font="TkFixedFont")
        self.entry_single_video_url.configure(foreground="#000000")
        self.entry_single_video_url.configure(highlightbackground="#d9d9d9")
        self.entry_single_video_url.configure(highlightcolor="black")
        self.entry_single_video_url.configure(insertbackground="black")
        self.entry_single_video_url.configure(selectbackground="#c4c4c4")
        self.entry_single_video_url.configure(selectforeground="black")

        self.label_1_title = tk.Label(self.Frame1)
        self.label_1_title.place(relx=0.4, rely=0.138, height=21, width=111)
        self.label_1_title.configure(activebackground="#f9f9f9")
        self.label_1_title.configure(activeforeground="black")
        self.label_1_title.configure(background="#d9d9d9")
        self.label_1_title.configure(disabledforeground="#a3a3a3")
        self.label_1_title.configure(foreground="#000000")
        self.label_1_title.configure(highlightbackground="#d9d9d9")
        self.label_1_title.configure(highlightcolor="black")
        self.label_1_title.configure(text='''Youtube Video URL:''')

        self.label_1_contact = tk.Label(self.Frame1)
        self.label_1_contact.place(relx=0.035, rely=0.828, height=21, width=141)
        self.label_1_contact.configure(activebackground="#f9f9f9")
        self.label_1_contact.configure(activeforeground="#afafaf")
        self.label_1_contact.configure(background="#d9d9d9")
        self.label_1_contact.configure(disabledforeground="#a3a3a3")
        self.label_1_contact.configure(foreground="#545454")
        self.label_1_contact.configure(highlightbackground="#d9d9d9")
        self.label_1_contact.configure(highlightcolor="black")
        self.label_1_contact.configure(text='''Contact: t.me/bisjutjopi''')

        self.label_3_version = tk.Label(self.Frame1)
        self.label_3_version.place(relx=0.035, rely=0.69, height=21, width=27)
        self.label_3_version.configure(activebackground="#f9f9f9")
        self.label_3_version.configure(activeforeground="black")
        self.label_3_version.configure(background="#d9d9d9")
        self.label_3_version.configure(disabledforeground="#a3a3a3")
        self.label_3_version.configure(foreground="#000000")
        self.label_3_version.configure(highlightbackground="#d9d9d9")
        self.label_3_version.configure(highlightcolor="black")
        self.label_3_version.configure(text='''v0.1''')

        self.button_download = tk.Button(self.Frame1)
        self.button_download.place(relx=0.783, rely=0.69, height=34, width=85)
        self.button_download.configure(activebackground="#ececec")
        self.button_download.configure(activeforeground="#000000")
        self.button_download.configure(background="#d9d9d9")
        self.button_download.configure(disabledforeground="#a3a3a3")
        self.button_download.configure(foreground="#000000")
        self.button_download.configure(highlightbackground="#d9d9d9")
        self.button_download.configure(highlightcolor="black")
        self.button_download.configure(pady="0")
        self.button_download.configure(text='''Download''')
        self.button_download.configure(command=self.start_YoutubeDL)

if __name__ == '__main__':
    vp_start_gui()





