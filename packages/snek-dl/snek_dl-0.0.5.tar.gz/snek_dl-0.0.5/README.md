# snek-dl

An intuitive wrapper for `youtube-dl`, to be used as a Python module.

## Installation
`pip install snek-dl`

## Why snek-dl?

`youtube-dl` is a very good CLI tool. However, it can be very confusing to use it within Python, despite being written
in Python. `snek-dl` aims to target that problem and make `youtube-dl` more intuitive to use in Python, 
right out of the box.  

### Okay, but seriously, why snek-dl?
1. Accurate URL retrieval
    * When `youtube-dl` uses `ffmpeg` to merge `.webm` and `.m4a` into a video-and-audio file format, the URL retrieved 
      from Python method `get_url()` is wrong: it only retrieves the audio URL.
    * `snek-dl` returns both the video and audio's URLs, accurately. 
       
2. Remedied inaccurate filename issue
    * Same issue as above: it's weirdly hard to get the output video file's name when `youtube-dl` uses `ffmpeg` to 
      merge the video and audio streams into one file. So it becomes extremely annoying to do any post-processing on the
      downloaded videos.
    * `snek-dl` returns the metadata after downloading the video, which includes basic information such as the actual
      correct filepath.
      
3. Readable, pretty output
    * Any information you `print()` for the sake of just looking at the output is so much more readable than the
      standard `youtube-dl` outputs.
    * Pretty-printing dictionaries and lists is built-in for humans, but it also does not affect any machines reading
      the objects.
      
And more to come! The more I use `youtube-dl` as a Python module, more weirdness I run into. I will be adding some of
the remedies for things that aren't smooth-sailing.

## Usage
```python
from snek_dl import Snek

# Initialize your snek engine
engine = Snek(
    url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    name_format="%(title)s-(%(format_id)s)-%(height)sp.%(ext)s", # ex) video_title-(22)-720p.mp4
    output_format="bestvideo[ext=mp4]" # picks the best video that has mp4 extension
)
```
```python
# or you can put youtube-dl's option dictionary
from snek_dl import Snek
opts = {
    "outtmpl": "%(title)s-(%(format_id)s)-%(height)sp.%(ext)s",
    "format": "bestvideo[ext=mp4]"
}
engine = Snek(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", options=opts)
```
```python
# with the initialized snek engine, you can retrieve info like metadata
from snek_dl import Snek
engine = Snek(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
# if you set download to false, it only retrieves metadata and does not trigger the download process.
# default is False
info = engine.info(download=False) # returns the metadata
# or if you only want one thing from the metadata:
info = engine.info_detail(detail="id") # returns the id

# there's a special method for retrieving and parsing available formats
# if you set full to true, it will return every detail. default is false
formats = engine.formats(full=False) # returns simplified formats
```
```python
# if you finished tweaking the engine, and want to start downloading:
from snek_dl import Snek

opts = {
    "outtmpl": "%(title)s-(%(format_id)s)-%(height)sp.%(ext)s",
    "format": "bestvideo[ext=mp4]"
}
engine = Snek(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", options=opts)
output = engine.download() # returns filename, id, url, format, and filesize after downloading
```
