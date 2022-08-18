from pytube import YouTube


def urlCheck(url):
    toCheck = url
    normalUrlHeader ="https://www.youtube.com/watch?"
    headerToCheck = url[0:len(normalUrlHeader)]
    check = -1

    if (headerToCheck == normalUrlHeader):
        check= 0
         
    return check

def downloadVideo():
    while True : 
        url = input("Paste Video URL:")
        if(urlCheck(url)!=0):
            print("Invalid URL, please try again")
            continue

        try:
            url = YouTube(url)
            break
        except :
            print("The video Could not be found, please try again with a different URL.")
            continue

    try:    
        video = url.streams.get_highest_resolution().download()
    except:
        print("ERROR downloading the Video")



		
		

 	    


        

    



