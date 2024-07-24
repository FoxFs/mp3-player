from tkinter import *
import pygame as pg
from tkinter import filedialog

root = Tk()
root.title("Mp3 Retro")
root.geometry("500x300")

pg.mixer.init()

# functions
def add_song():
    song = filedialog.askopenfilename(initialdir='MP3 2.0\music', title="Choose song", filetypes=[("mp3 Files", "*.mp3")])
    song_name =song.split('/')[-1].split('.')[0]
    song_box.insert(END, song_name)

def play():
    song = song_box.get(ACTIVE)
    song = f'MP3 2.0\music\{song}.mp3'

    pg.mixer.music.load(song)
    pg.mixer.music.play(loops=0)

def stop():
    pg.mixer_music.stop()
    song_box.selection_clear(ACTIVE)
    
# Song list
song_box = Listbox(root, bg="oliveDrab", fg="black", width=60, selectbackground="YellowGreen", )
song_box.pack(pady=20)

# images buttons
back_img = PhotoImage(file='MP3 2.0\images\skipleft_button.png')
forward_img = PhotoImage(file='MP3 2.0\images\skipright_button.png')
play_img = PhotoImage(file='MP3 2.0\images\play_button.png')
stop_img = PhotoImage(file='MP3 2.0\images\Stop_button.png')
pause_img = PhotoImage(file='MP3 2.0\images\pause_button.png')

# Player buttons
controls_frame = Frame(root)
controls_frame.pack()

back_bnt = Button(controls_frame, image=back_img, borderwidth=0)
forward_bnt = Button(controls_frame, image=forward_img, borderwidth=0)
play_bnt = Button(controls_frame, image=play_img, borderwidth=0, command=play)
pause_bnt = Button(controls_frame, image=pause_img, borderwidth=0)
stop_btn = Button(controls_frame, image=stop_img, borderwidth=0, command=stop)

back_bnt.grid(row=0, column=0, padx=10)
forward_bnt.grid(row=0, column=1, padx=10)
play_bnt.grid(row=0, column=2, padx=10)
pause_bnt.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

#menu
themenu = Menu(root)
root.config(menu=themenu)
add_song_menu = Menu(themenu)
themenu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Songs", command=add_song)

root.mainloop()