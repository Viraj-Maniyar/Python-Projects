from pytube import YouTube

link = "https://www.youtube.com/watch?v=8TttGS0zrE8"
youtube_1 = YouTube(link)

print(youtube_1.title)
print(youtube_1.thumbnail_url)

videos = youtube_1.streams.all() # all format
# videos = youtube_1.streams.filter(only_audio=True)  # only audio format
vid = list(enumerate(videos))

for i in vid:
    print(i)
strm = int(input("enter: "))
videos[strm].download()
print("Downloaded successfully")