# Youtube to MP3

This program was built using [PAGE][4] based on the idea of [ripping][3] Youtube video to Mp3 audio file.

### Required Files

- Latest [youtube-dl][1] executable file
- ffmpeg and ffprobe [executable files][2]

Put all files in the same path as `youtubedl.py`

### Modifying the GUI

1. Download and install [PAGE][4]
2. Read its instructions on how to use, you might need to install Tcl/Tk 8.6 or greater
3. Open `youtubedl.tcl` file

### Creating an exe file

```
pyinstaller -F -w youtubedl.py
```

#### TODO

- Real-time progress in widget
- Disable text field while downloading
- Options for batch download

#### Changelog:

**v0.1**
- Able to download a single video as MP3

--- 

Aiman Baharum (2019)

[1]: https://github.com/rg3/youtube-dl/releases
[2]: https://ffbinaries.com/downloads
[3]: https://blog.aimanbaharum.com/2017/12/12/ripping-youtube-videos-to-mp3-using-command-prompt/
[4]: http://page.sourceforge.net/
[5]: https://www.activestate.com/products/activetcl/downloads/