from tkinter import *
import os
import io
import sys
import ctypes
from math import log10
import win32gui
import win32con
import win32api
from PIL import Image, ImageTk
from mutagen import File
import win32com.client

# Connect to foobar2k
program = "Foobar2000.Application.0.7"
try:
    f2k = win32com.client.Dispatch(program)
except Exception:
    win32api.MessageBox(
        0, "Could not connect to f2k COM server.", "FoobarMiniplayer - Error"
    )
    sys.exit()

playback = f2k.Playback

# Fallback values for settings
col_bg = "#000000"
col_fg = "#bada55"
position = (10, 10)
alpha = 0.6


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, background=col_bg)
        self.timer = 0
        self.paused = playback.IsPaused

        self.np = self.get_np()  # Now playing
        self.np_len = len(self.np)

        self.marquee_text = StringVar()
        self.marquee_text.set(self.np)
        self.marquee_shift = 0

        self.path = self.get_path()
        self.alb_art = self.get_art()
        self.load_images()

        self.pack(fill=BOTH, expand=1)
        self.create_widgets()

        # Bind keys/buttons
        self.art_lbl.bind("<Button-1>", self.focus_fb)
        self.art_lbl.bind("<ButtonRelease-3>", self.save_and_quit)
        self.master.bind("<ButtonPress-2>", self.start_move)
        self.master.bind("<ButtonRelease-2>", self.stop_move)
        self.master.bind("<B2-Motion>", self.on_motion)
        self.master.bind("<Control-c>", self.copy_track)

        self.updater()

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def on_motion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.master.winfo_x() + deltax
        y = self.master.winfo_y() + deltay

        self.master.geometry("+%s+%s" % (x, y))

    def create_widgets(self):
        # Add album art
        self.art_lbl = Label(
            self, image=self.alb_art, bd=0, highlightthickness=0
        )
        self.art_lbl.place(x=0, y=0)

        # Add a randomise button
        self.rand_btn = Button(
            self,
            image=self.rand_img,
            bd=0, highlightthickness=0,
            command=playback.Random
        )
        self.rand_btn.place(x=40, y=15)

        # Add a previous track button
        self.prev_btn = Button(
            self,
            image=self.prev_img,
            bd=0,
            highlightthickness=0,
            command=playback.Previous
        )
        self.prev_btn.place(x=65, y=15)

        # Add a play/pause button with correct initial graphic
        if playback.IsPaused:
            img = self.play_img
        else:
            img = self.pause_img
        self.playpause_btn = Button(
            self, image=img, bd=0, highlightthickness=0, command=playback.Pause
        )
        self.playpause_btn.place(x=90, y=15)

        # Add a next track button
        self.next_btn = Button(
            self,
            image=self.next_img,
            bd=0,
            highlightthickness=0,
            command=playback.Next
        )
        self.next_btn.place(x=115, y=15)

        # Add a volume slider
        self.vol_scl = Scale(
            self,
            orient=HORIZONTAL,
            showvalue=0,
            sliderrelief=FLAT,
            highlightthickness=0,
            bd=0,
            width=23, length=46,
            sliderlength=8,
            from_=1, to=100,
            bg=col_fg,
            troughcolor=col_bg,
            activebackground=col_fg,
            command=self.vol_update
        )
        self.vol_scl.place(x=140, y=16)
        vol = playback.Settings.Volume
        vol = ((vol / 100 + 2) ** 10) / 10  # Convert from log to linear
        self.vol_scl.set(vol)

        # Add a text label
        self.marquee_lbl = Label(
            self,
            textvariable=self.marquee_text,
            bg=col_bg, fg=col_fg,
            highlightthickness=0, bd=0,
            padx=1, pady=0,
            font=("Tahoma", "8")
        )
        self.marquee_lbl.place(x=40, y=0)

    def updater(self):
        if playback.IsPaused != self.paused:
            if playback.IsPaused:
                self.playpause_btn.configure(image=self.play_img)
            else:
                self.playpause_btn.configure(image=self.pause_img)

        if self.marquee_lbl.winfo_width() > 142:
            # Short strings wont need to be marqueed
            np_shifted = (self.np[self.marquee_shift:]
                          + ", "
                          + self.np[:self.marquee_shift])
            self.marquee_text.set(np_shifted)

        # 1 iteration per 250ms, 24/4 = 6 seconds
        if self.timer > 24:
            # Sometimes a window might steal topmost
            self.master.wm_attributes("-topmost", 1)
            self.timer = 0

        new_np = self.get_np()

        if self.np != new_np and playback.IsPlaying:
            self.path = self.get_path()
            self.np = self.get_np()
            self.np_len = len(self.np)
            self.marquee_text.set(self.np)
            self.marquee_shift = 0
            self.alb_art = self.get_art()
            self.art_lbl.configure(image=self.alb_art)

        # Update timers/counters
        if self.marquee_lbl.winfo_width() > 142 and not playback.IsPaused:
            # Marquee stops while paused
            self.marquee_shift += 1
        if self.marquee_shift > self.np_len:
            self.marquee_shift = 0

        self.timer += 1
        self.paused = playback.IsPaused

        self.after(250, self.updater)

    def load_images(self):
        play_image = Image.open(os.getcwd()+"\\res\\btn_play.png")
        self.play_img = ImageTk.PhotoImage(play_image)

        pause_image = Image.open(os.getcwd()+"\\res\\btn_pause.png")
        self.pause_img = ImageTk.PhotoImage(pause_image)

        prev_image = Image.open(os.getcwd()+"\\res\\btn_prev.png")
        self.prev_img = ImageTk.PhotoImage(prev_image)

        next_image = Image.open(os.getcwd()+"\\res\\btn_next.png")
        self.next_img = ImageTk.PhotoImage(next_image)

        rand_image = Image.open(os.getcwd()+"\\res\\btn_rand.png")
        self.rand_img = ImageTk.PhotoImage(rand_image)

    def vol_update(self, event):
        percent = self.vol_scl.get()
        db = (log10(percent) / 2 * 100) - 100
        playback.Settings.Volume = db

    def get_path(self):
        return playback.FormatTitle("[%path%]")

    def get_np(self):
        # Find current artist/track
        if playback.isPlaying:
            artist = str(playback.FormatTitle("[%artist%]"))
            if len(artist) == 0:
                artist = "Unknown"
            track = str(playback.FormatTitle("[%title%]"))
            if len(track) == 0:
                track = "Unknown"
        else:
            artist = "Unknown"
            track = "Unknown"

        return artist+" :: "+track

    def get_art(self):
        found_art = False
        art_files = [
            "folder.jpg", "folder.png", "folder.gif", "cover.png",
            "cover.jpg", "cover.gif", "front.jpg", "front.png", "front.gif"
        ]
        folder, filename = os.path.split(self.path)

        for filename in art_files:
            if os.path.isfile(folder+"\\"+filename):
                img = Image.open(folder+"\\"+filename)
                found_art = True

        if not found_art:
            try:
                file = File(self.path)
                # Access APIC frame and grab bytes
                art_bytes = file.tags["APIC:"].data
                # Create new PIL image from bytes
                img = Image.open(io.BytesIO(art_bytes))
                found_art = True
            except Exception:
                pass

        if found_art and img is not None:
            # Resize image
            img = img.resize((40, 40), Image.ANTIALIAS)
        else:
            img = Image.open("res\\album_art.png")

        return ImageTk.PhotoImage(img)

    def focus_fb(self, event=None):
        toplist = []
        winlist = []

        def enum_callback(hwnd, results):
            winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

        win32gui.EnumWindows(enum_callback, toplist)
        foobar = [(hwnd, title) for hwnd, title in winlist
                  if "foobar2000" in title.lower()]
        foobar = foobar[0]

        win32gui.ShowWindow(foobar[0], win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(foobar[0])

    def save_and_quit(self, event=None):
        x = self.master.winfo_x()
        y = self.master.winfo_y()

        with open(os.getcwd() + "\\config.ini", "r") as config:
            data = config.readlines()
        i = 0
        for line in data:
            if "position" in line:
                data[i] = "position="+str(x)+","+str(y)+"\n"
            i += 1

        with open(os.getcwd() + "\\config.ini", "w") as config:
            config.writelines(data)
        config.close()
        sys.exit()

    def copy_track(self, event=None):

        self.clipboard_clear()
        self.clipboard_append(self.np)


def check_aero():
    try:
        b = ctypes.c_bool()
        retcode = ctypes.windll.dwmapi.DwmIsCompositionEnabled(ctypes.byref(b))
        return retcode == 0 and b.value
    except AttributeError:
        # No windll, no dwmapi or no DwmIsCompositionEnabled function.
        return False


def load_config():
    global position, alpha, col_fg, col_bg

    with open(os.getcwd() + "\\config.ini") as config:
        for line in config:
            if "position" in line:
                x_loc = line.find("=")+1
                y_loc = line.find(",")+1
                x = int(line[x_loc:y_loc-1].strip())
                y = int(line[y_loc:].strip())
                position = (x, y)
            if "alpha" in line:
                alpha = float(line[line.find("=")+1:].strip())
            if "col_fg" in line:
                col_fg = line[line.find("#"):].strip()
            if "col_bg" in line:
                col_bg = line[line.find("#"):].strip()
    config.close()
    return


def main():
    load_config()

    root = Tk()
    root.geometry("187x40+"+str(position[0])+"+"+str(position[1]))
    root.resizable(0, 0)
    if check_aero():
        root.attributes("-alpha", alpha)
    root.wm_attributes("-topmost", 1)
    root.attributes("-toolwindow", 1)
    root.overrideredirect(True)

    app = Application(root)
    app.master.title("f2k Mini Player")

    root.mainloop()


if __name__ == "__main__":
    main()
