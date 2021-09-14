from tkinter import *

root=Tk()
root.geometry("500x200")
root.title("KALAv1")
e=Entry(root)
e.insert(0,"")
e.pack()
f=Entry(root)
f.insert(1,"")
f.pack()

def encrypt():
    text=e.get()
    convertvideo(download_video(get_link(text)))
    myLabel=Label(root,text="Saved as "+f.get())
    myLabel.pack()

def get_link(title):
    import os
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    
    browser = webdriver.Chrome(os.getcwd()+"\\chromedriver")
    browser.get("https://www.youtube.com/results?search_query="+title)
    
    browser.find_element_by_id("img").click()
    address = browser.current_url
    browser.quit()
    return address
def download_video(address):
    from pytube import YouTube
    out_file = YouTube(address).streams.first().download(filename="video")
    return out_file
def convertvideo(location):
    import moviepy.editor
    import os
    video = location
    video = moviepy.editor.VideoFileClip(video)
    audio = video.audio
    audio.write_audiofile(f.get()+".mp3")
    
    


def install():
    import pip
    import os
    package=['selenium', 'moviepy', 'pytube']
    for i in package:
        if hasattr(pip, 'main'):
            pip.main(['install', i])
        else:
            pip._internal.main(['install', j])

    res="Pre-requisite satisfied"
    myLabel=Label(root,text=res)
    myLabel.pack()


myButton1=Button(
    root,
    text="Pre-requisite",
    command=install)
    
myButton2=Button(
    root,
    text="Download",
    command=encrypt)


myButton1.pack()
myButton2.pack()
myLabel=Label(root,text="Note: run-second only if you are done with downloading and close this before using that")
myLabel.pack()
root.mainloop()
