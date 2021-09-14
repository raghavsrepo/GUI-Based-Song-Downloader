import os
import shutil
current = os.getcwd()+"\\"
dest = os.getcwd()+"\\Music\\"
for i in os.listdir():
        if 'mp3' in i:
                shutil.move(current+i, dest+i)
        if i == "video":
                os.remove("video")
                
