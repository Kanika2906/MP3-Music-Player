from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer
from tkinter import ttk

# colors
col1 = "#ffffff"       # white
col2 = "#3C1DC6"       # purple
col3 = "#333333"       # black
col4 = "#CFC7F8"       # light purple

window = Tk()
window.title("MP3 Music Player")
window.geometry("380x275")
window.configure(background=col1)
window.resizable(height=False, width=False)

# frames
left_frame = Frame(window, width=150, height=150, bg=col1)
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = Frame(window, width=250, height=150, bg=col3)
right_frame.grid(row=0, column=1, padx=0, pady=0)

down_frame = Frame(window, width=400, height=115, bg=col4)
down_frame.grid(row=1, column=0, padx=0, pady=1, columnspan=2)


# right_frame
listbox = Listbox(
    right_frame,
    selectmode=SINGLE,
    font=("Arial 9 bold"),
    width=22,
    bg=col3,
    fg=col1
)

listbox.grid(row=0, column=0)

w = Scrollbar(right_frame)
w.grid(row=0, column=1, sticky="ns")

listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview)


# Events

def play_music():
    running = listbox.get(ACTIVE)

    running_song['text'] = running

    mixer.music.load("music/" + running)
    mixer.music.play()


def pause_music():
    mixer.music.pause()


def continue_music():
    mixer.music.unpause()


def stop_music():
    mixer.music.stop()


def next_music():
    playing = running_song['text']

    if playing == "Choose a song":
        return

    index = songs.index(playing)

    if index < len(songs) - 1:
        new_index = index + 1
    else:
        new_index = 0

    playing = songs[new_index]

    running_song['text'] = playing

    listbox.selection_clear(0, END)
    listbox.selection_set(new_index)
    listbox.activate(new_index)

    mixer.music.load("music/" + playing)
    mixer.music.play()


def prev_music():
    playing = running_song['text']

    if playing == "Choose a song":
        return

    index = songs.index(playing)

    if index > 0:
        new_index = index - 1
    else:
        new_index = len(songs) - 1

    playing = songs[new_index]

    running_song['text'] = playing

    listbox.selection_clear(0, END)
    listbox.selection_set(new_index)
    listbox.activate(new_index)

    mixer.music.load("music/" + playing)
    mixer.music.play()


# Volume function
def set_volume(value):
    volume = float(value) / 100
    mixer.music.set_volume(volume)


# images

img1 = Image.open('images/image.png')
img1 = img1.resize((130, 130))
img1 = ImageTk.PhotoImage(img1)

app_image = Label(
    left_frame,
    height=150,
    width=150,
    image=img1
)

app_image.place(x=0, y=0)


# Previous
img2 = Image.open('images/backward.png')
img2 = img2.resize((30, 30))
img2 = ImageTk.PhotoImage(img2)

prev_image = Button(
    down_frame,
    height=40,
    width=40,
    image=img2,
    padx=10,
    bg=col1,
    font=("Ivy 10"),
    command=prev_music
)

prev_image.place(x=10+28, y=35)


# Play
img3 = Image.open('images/play.png')
img3 = img3.resize((30, 30))
img3 = ImageTk.PhotoImage(img3)

play_image = Button(
    down_frame,
    height=40,
    width=40,
    image=img3,
    padx=10,
    bg=col1,
    font=("Ivy 10"),
    command=play_music
)

play_image.place(x=56+28, y=35)


# Pause
img4 = Image.open('images/pause.png')
img4 = img4.resize((30, 30))
img4 = ImageTk.PhotoImage(img4)

pause_image = Button(
    down_frame,
    height=40,
    width=40,
    image=img4,
    padx=10,
    bg=col1,
    font=("Ivy 10"),
    command=pause_music
)

pause_image.place(x=102+28, y=35)


# Stop
img5 = Image.open('images/stop.png')
img5 = img5.resize((30, 30))
img5 = ImageTk.PhotoImage(img5)

stop_image = Button(
    down_frame,
    height=40,
    width=40,
    image=img5,
    padx=10,
    bg=col1,
    font=("Ivy 10"),
    command=stop_music
)

stop_image.place(x=148+28, y=35)


# Continue
img6 = Image.open('images/continue.png')
img6 = img6.resize((30, 30))
img6 = ImageTk.PhotoImage(img6)

continue_image = Button(
    down_frame,
    height=40,
    width=40,
    image=img6,
    padx=10,
    bg=col1,
    font=("Ivy 10"),
    command=continue_music
)

continue_image.place(x=194+28, y=35)


# Next
img7 = Image.open('images/forward.png')
img7 = img7.resize((30, 30))
img7 = ImageTk.PhotoImage(img7)

forward_image = Button(
    down_frame,
    height=40,
    width=40,
    image=img7,
    padx=10,
    bg=col1,
    font=("Ivy 10"),
    command=next_music
)

forward_image.place(x=240+28, y=35)


# Running song
running_song = Label(
    down_frame,
    text="Choose a song",
    width=47,
    font=("Ivy 10"),
    height=1,
    padx=10,
    bg=col1,
    fg=col3,
    anchor=NW
)

running_song.place(x=0, y=1)


# Music files
songs = os.listdir('music')


def show():
    for i in songs:
        listbox.insert(END, i)


show()


# Initialize mixer
mixer.init()


# Volume image
img8 = Image.open('images/volume.png')
img8 = img8.resize((27, 27))
img8 = ImageTk.PhotoImage(img8)

volume_image = Label(
    down_frame,
    image=img8,
    bg=col4
)

volume_image.place(x=105, y=84)

style = ttk.Style()

style.configure(
    "Volume.Horizontal.TScale",
    background=col4
)

volume_scale = ttk.Scale(
    down_frame,
    from_=0,
    to=100,
    orient=HORIZONTAL,
    length=120,
    command=set_volume
)

volume_scale.set(70)
volume_scale.place(x=135, y=86)


music_state = StringVar()
music_state.set("Choose one!")

window.mainloop()