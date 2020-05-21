# Youtube to MP3 Ripper

![screenshot v0.1](https://i.imgur.com/yZ9i2B5.jpg)

This program was built using [PAGE][4] based on the idea of ripping Youtube video to an Mp3 audio file set to the highest quality.

### Required Files

- Latest [youtube-dl][1] executable file
- ffmpeg and ffprobe [executable files][2]

Put all files in the same path as `youtubedl.py`

### Modifying the GUI

1. Download and install [PAGE][4]
2. Read its instructions on how to use, you might need to install _Tcl/Tk 8.6 or greater_
3. Open `youtubedl.tcl` file

### Creating an exe file (for Windows)

```
pyinstaller -F -w youtubedl.py
```

#### TODO

- Real-time progress in widget
- Options for batch download
- Custom youtube-dl args (make optional? this will enable video as well)
- Cross-platform (Linux, Windows, Mac)

#### Changelog:

**v0.1**
- Able to download a single video as MP3 highest quality
- Current static arguments `youtube-dl.exe --extract-audio --output \"%(title)s.%(ext)s\" --audio-format mp3 --audio-quality 0`

--- 

Aiman (2020)

[1]: https://github.com/rg3/youtube-dl/releases
[2]: https://ffbinaries.com/downloads
[4]: http://page.sourceforge.net/
[5]: https://www.activestate.com/products/activetcl/downloads/