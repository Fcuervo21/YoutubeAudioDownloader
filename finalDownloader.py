from pytube import YouTube
import os

# url input from user
entry_url = input("Enter the URL of the video you want to download: ")
yt = YouTube(entry_url)
  
# extract only audio
#video = yt.streams.filter(only_audio=True).first()
video = yt.streams.get_audio_only()
  
# check for destination to save file
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'
  
# download the file
out_file = video.download(output_path=destination)
  
# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp4'
os.rename(out_file, new_file)
  
# result of success
print(yt.title + " has been successfully downloaded.")

# if __name__ == "__main__":
#     pass