from tkinter import *
import pygame as pg
from tkinter import filedialog
import time
from mutagen.mp3 import MP3

root = Tk()
root.title("Mp3 Retro")
root.geometry("500x300")

pg.mixer.init()

#this gonna show the bar
def play_time():
    current_time = pg.mixer.music.get_pos() / 1000

    convert_current_time = time.strftime('%M:%S', time.gmtime(current_time))

    #get a lenght song
    song = song_box.get(ACTIVE)
    song = f'MP3 2.0\music\{song}.mp3'

    song_mut = MP3(song)
    song_length = song_mut.info.length
    convert_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    #output time just it
    status_bar.config(text=f'time elapsed {convert_current_time} of {convert_song_length} ')

    #update the time always
    status_bar.after(1000, play_time)


# functions
def add_songs():
    songs = filedialog.askopenfilenames(initialdir='MP3 2.0\music', title="Choose song", filetypes=[("mp3 Files", "*.mp3")])
    for song in songs:
        song_name =song.split('/')[-1].split('.')[0]
        song_box.insert(END, song_name)


def play():
    song = song_box.get(ACTIVE)
    song = f'MP3 2.0\music\{song}.mp3'

    pg.mixer.music.load(song)
    pg.mixer.music.play(loops=0)

    #call the playtime function
    play_time()

def stop():
    pg.mixer_music.stop()
    song_box.selection_clear(ACTIVE)

    status_bar.config(text='')

#this a globol variable, what determine everything its paused, and when this paused. if u press again its be unpause
global paused
paused = False

def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pg.mixer.music.unpause()
        paused = False

    else:
        pg.mixer.music.pause()
        paused = True

def next_song():
    next_musc = song_box.curselection()
    #this gonna get the music and forward also
    next_musc = next_musc[0] + 1

    song = song_box.get(next_musc)
    song = f'MP3 2.0\music\{song}.mp3'

    pg.mixer.music.load(song)
    pg.mixer.music.play(loops=0)

    #clear the seletcion bar
    song_box.select_clear(0, END)

    #active bar selection
    song_box.activate(next_musc)

    #set a bar to next song
    song_box.selection_set(next_musc, last=None)


def back_song():
    back_musc = song_box.curselection()
    #this get a music in the list (songbox) and return - 1 in the playlist
    back_musc = back_musc[0] - 1

    song = song_box.get(back_musc)
    song = f'MP3 2.0\music\{song}.mp3'

    #this the same thing in play function
    pg.mixer.music.load(song)
    pg.mixer.music.play(loops=0)

    #clear the seletcion bar
    song_box.select_clear(0, END)

    #active bar selection
    song_box.activate(back_musc)

    #set a bar to next song
    song_box.selection_set(back_musc, last=None)


def delete_songs():
    #this wanna delete the current music selection
    song_box.delete(ANCHOR)

    #this stop the music after it´s del
    pg.mixer.music.stop()

def delete_allsongs():
    #this wanna delete everything
    song_box.delete(0, END)

    #take a note, yeah....this stop the music too
    pg.mixer.music.stop()

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

back_bnt = Button(controls_frame, image=back_img, borderwidth=0, command=back_song)
forward_bnt = Button(controls_frame, image=forward_img, borderwidth=0, command=next_song)
play_bnt = Button(controls_frame, image=play_img, borderwidth=0, command=play)
pause_bnt = Button(controls_frame, image=pause_img, borderwidth=0, command=lambda: pause(paused))
stop_btn = Button(controls_frame, image=stop_img, borderwidth=0, command=stop)

back_bnt.grid(row=0, column=0, padx=10)
forward_bnt.grid(row=0, column=4, padx=10)
play_bnt.grid(row=0, column=1, padx=10)
pause_bnt.grid(row=0, column=2, padx=10)
stop_btn.grid(row=0, column=3, padx=10)

#menu
themenu = Menu(root)
root.config(menu=themenu)
add_song_menu = Menu(themenu)
themenu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Songs", command=add_songs)

#menu song remove:
remove_song_menu = Menu(themenu)
themenu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a song", command=delete_songs)
remove_song_menu.add_command(label="Delete all song", command=delete_allsongs)


#this is a status bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

root.mainloop()