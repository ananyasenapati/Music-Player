import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os
from tkinter import Scale 

root=Tk()
root.title("simple music player")
root.geometry("485x700+290+10") 
root.configure(background="#333333")
root.resizable(False,False) 
mixer.init()
frameCnt = 30
frames = [PhotoImage(file='aa1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)
label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)
def AddMusic():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END,song)
def PlayMusic():
    Music_Name=Playlist.get(ACTIVE)
    print(Music_Name)
    mixer.music.load(Music_Name)
    mixer.music.play()    
def PauseMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name)
    mixer.music.pause()
def set_volume(val):
    volume = int(val) / 100  # Convert scale value to a percentage
    mixer.music.set_volume(volume)



       
lower_frame= Frame(root, bg="#FFFFFF", width=485, height=180)
lower_frame.place(x=0,y=400) 
image_icon=PhotoImage(file="logo2.png")
root.iconphoto(False,image_icon)
Menu=PhotoImage(file="Solid_white.png")
Label(root,image=Menu).place(x=0,y=580,width=485,height=100)
Frame_Music=Frame(root,bd=2,relief=RIDGE)
Frame_Music.place(x=0,y=585,width=485,height=100)
ButtonPlay=PhotoImage(file="download.png")
Button(root,image=ButtonPlay, bg="#FFFFFF", bd=0,height=60,width=60,command=PlayMusic).place(x=215,y=487)
ButtonStop=PhotoImage(file="stopup.png")
Button(root,image=ButtonStop, bg="#FFFFFF", bd=0,height=60,width=60,command=mixer.music.stop).place(x=130,y=487)
ButtonPause=PhotoImage(file="pauseup.png")
Button(root,image=ButtonPause, bg="#FFFFFF", bd=0,height=60,width=60,command=mixer.music.pause).place(x=300,y=487)
Volume1=PhotoImage(file="volumegit.png")
panel=Label(root,image=Volume1).place(x=20,y=487)
volume_scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
volume_scale.set(50)  # Set initial volume to 50%
volume_scale.place(x=80, y=500)



Button(root,text="Browse Music",width=59,height=1,font=('calibri',12,"bold"),fg="Black",bg="#FFFFFF", command=AddMusic).place(x=0,y=550)


Scroll=Scrollbar(Frame_Music)
Playlist=Listbox(Frame_Music,width=100,font=("Times new roman",10),bg="#333333",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT,fill=Y)
Playlist.pack(side=RIGHT,fill=BOTH)
root.mainloop()



