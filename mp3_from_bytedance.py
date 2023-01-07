import csv
import requests
# importing packages
from pytube import YouTube
import os
import time
import requests
st = time.time()


def try_site(url):
    request = requests.get(url)
    pattern = '"playabilityStatus":{"status":"ERROR","reason":"Video unavailable"'
    return False if pattern in request.text else True
# opening the CSV file
newpath = r'.\ALL_MP3'
illegal=['#','%','&','{','}','\\','<','>','*','?','/',
         '$','!',"'",'"',':','@','+','`','|','=',' ','-']
with open('full_music_pieces_youtube_similarity_pianosoloprob_split.csv', encoding="utf8")as file:
   
  # reading the CSV file
    csvFile = csv.reader(file)
 
  # displaying the contents of the CSV file
    i=0
    for lines in csvFile:
        
        if i==100:
            break
        current=lines[0]
        current=current.split('\t')
        currsite='https://www.youtube.com/watch?v='+current[7])
     
        if (len(current)>7 and try_site(currsite)):
            for ill in illegal:
                current[6]=current[6].replace(ill,'_')
            newpath = r".\All_MP3\\"+current[6]+str(i)
            yt=YouTube(currsite)
            
            # extract only audio
            video = yt.streams.filter(only_audio=True).first()
            # download the file
            #print(yt.title + " start.")
            out_file = video.download(output_path=newpath)
            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            #print(yt.title + " has been successfully downloaded.")
        i+=1
et = time.time()
print(et-st)
#
            
