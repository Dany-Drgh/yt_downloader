from pytube import YouTube
from art import tprint 

tprint("Youtube Downloader")
print("Welcome to Youtube Downloader V.1.0 \n")

while True : 
    url = input("Paste Video URL:")
    try:
        url = YouTube(url)
        break
    except :
        print("Something went wrong, please try again.")
        continue

try:    
    video = url.streams.get_highest_resolution().download()
except:
    print("ERROR downloading the Video")



