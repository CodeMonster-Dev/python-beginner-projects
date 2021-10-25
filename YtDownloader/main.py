from pytube import YouTube

#ask user for youtube video link

link = input("Enter YouTube video link which you want to download")
yt = YouTube(link)

print("Title:", yt.title)
print("Description", yt.description)
print("# of Views", yt.views)
print("Length of Video", yt.length)
print("Rating of Video", yt.rating)

#Getting the highest resolution to download video


ys = yt.streams.get_highest_resolution()

#Starting Download

print("Downloading Start...")

ys.download()

print("Download Completed")