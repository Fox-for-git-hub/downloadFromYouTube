from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=qLYmtdi-GzA&list=RDqLYmtdi-GzA&start_radio=1')
stream = yt.streams.first()
finished = stream.download()
