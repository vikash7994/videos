from __future__ import unicode_literals
import youtube_dl
import json
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    url = ydl.extract_info('https://www.facebook.com/watch?v=1449784095787165',download=False)
    print(url['formats'][-1][url])