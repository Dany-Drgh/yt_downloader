import os
from pytube import YouTube



def urlCheck(url):
# Checks if url has the YT video url header format
    toCheck = url
    normalUrlHeader ="https://www.youtube.com/watch?"
    headerToCheck = url[0:len(normalUrlHeader)]
    check = -1

    if (headerToCheck == normalUrlHeader):
        check= 0
         
    return check

def downloadPrep():
# Gets Url from user and Checks if Youtube video is reachable and returns URL 
   
    while True : 
        url = input("Paste Video URL:")
        if(urlCheck(url)!=0):
            print("Invalid URL, please try again")
            continue

        try:
            url = YouTube(url)
            return url
        except :
            #If video is not reachable try loop back and ask for new URL
            print("The video Could not be found, please try again with a different URL.")
            continue

def downloadVideo():

    url = downloadPrep()
    try:    
        video = url.streams.get_highest_resolution().download()
    except:
        print("ERROR downloading the Video")

def downloadAudio():
    url = downloadPrep()

    try:    
        video = url.streams.filter(only_audio=True)
        video[0].download()
        old = url.title+".mp4"
        new = url.title+".mp3"
        os.rename(old, new)
    except:
        print("ERROR downloading the Audio file")


# Menu functions

def menu():
    while True :
        print("\n1. Donwload a Full Video in .mp4 format")
        print("2. Only Get Audio File from a video in .mp3 format ")
        print("3. Close")

        choice = str(input("Please type your choice: \n"))
    
        if choice == "1":
            downloadVideo()
            continue
        elif choice == "2":
            downloadAudio()
            continue
        elif choice == "3":
            print("Thank you for using YoutubeDownloader !")
            break
        else: 
            print(f'{choice} is not a Valide input, please try again.\n')
            continue
            
            
    



		
		

 	    


        

    



