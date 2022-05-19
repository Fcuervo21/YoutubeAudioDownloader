from pytube import YouTube
import os

# url input from user
def downloadSong(link):
    #entry_url = input("Enter the URL of the video you want to download: ")
    yt = YouTube(link)
    
    # extract only audio
    #video = yt.streams.filter(only_audio=True).first()
    video = yt.streams.get_audio_only()
    
    # # check for destination to save file
    # print("Enter the destination (leave blank for current directory)")
    # destination = str(input(">> ")) or '.'
    
    # download the file
    out_file = video.download(output_path='.')
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)
    
    # result of success
    print(yt.title + " has been successfully downloaded.")

if __name__ == "__main__":
    my_file = open("YOUR TXT FILE PATH", "r")
    content = my_file.read().split("\n")
    print("The songs you placed in the file are about to be downloaded...\n")
    for i in content:
        downloadSong(i)
