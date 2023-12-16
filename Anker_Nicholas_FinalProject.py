#SV140 Final Project
#Nicholas Anker
#2023/12/03
#Create a working GUI application with tkinter.

"""
import tkinter features

create main window
    self.geometry
    self.title
    self.config
    set labels
    set button to second window
    set button to close
    set image

create second window
    self.geometry
    self.title
    self.config
    set labels
    set entry fields
    set button to send data
    set button to close window
    set image

create loop
"""


#import module and tools
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

 

#second window
class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        #size, title, color, text entry, and buttons
        self.geometry('400x400')
        self.title('Record Request')
        self.configure(bg="#7FFFD4")
        #set variables
        email = tk.StringVar()
        artist = tk.StringVar()
        album = tk.StringVar()
        #create function to inform user that it went through
        def submit_request():
            msg = f'You entered {email.get()}, {artist.get()}, {album.get()}'
            showinfo(title= 'Thanks!', message = msg)
        #create function to save data to a .txt file    
        def submit_data():
            try:
                #use try/except for error handling
                f = open("recordrequest.txt", 'a')
                f.write(f'\n{email.get()}, {artist.get()}, {album.get()}')
                f.close()
            except:
                error = 'Something went wrong, please try again.'
                showerror(title='Error', message = error)
        
        #label and entry box linking to 'email' variable    
        email = tk.StringVar()
        email_label = ttk.Label(self, text="Email:")
        email_label.pack(fill='x')
        email_entry = ttk.Entry(self, textvariable=email)
        email_entry.pack(fill='x')
        email_entry.focus()                     
        #label and entry box linking to 'artist' variable
        artist = tk.StringVar()
        artist_label = ttk.Label(self, text="Artist:")
        artist_label.pack(fill='x')
        artist_entry = ttk.Entry(self, textvariable=artist)
        artist_entry.pack(fill='x')
        artist_entry.focus()
        #label and entry box linking to 'album' variable
        album = tk.StringVar()
        album_label = ttk.Label(self, text="Album:")
        album_label.pack(fill='x')
        album_entry = ttk.Entry(self, textvariable=album)
        album_entry.pack(fill='x')
        album_entry.focus()
        #setup button to display message, send data, then close window
        ttk.Button(self, text="Submit Request", command= lambda:[submit_request(), submit_data(), self.destroy()]).pack( fill='x', pady=10)
        ttk.Button
        close_button = ttk.Button(self,
                text='Close',
                command=self.destroy).pack(expand=True)
                #button closes window
        
#main window
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #size, title, color, slogan, button leading to second window
        self.geometry('400x400')
        self.title('Rockin Records')
        self.configure(bg="#7FFFD4")
        #tktext_label.image = "Guitar.png"
        #I tried importing a picture, but couldn't figure it out
        #Button to open second window
        ttk.Button(self,
                text='Click here to request an album or artist!',
                command=self.open_window).pack(side=tk.TOP, expand=True)
        ttk.Button(self,
                text='Close',
                command=self.destroy).pack(side=tk.BOTTOM, expand=True)
                #button closes window
#sets up as a function
    def open_window(self):
        window = Window(self)
        window.grab_set()

#sets up main loop
if __name__ == "__main__":
    app = App()
    app.mainloop()
