from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Error has ocorred")
    print("Download completed successfully")

link = input("Enter the Youtube video URL: ")
Download(link)