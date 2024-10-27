# Youtube Converter ------------------------------------------------------------------------------------
# This Program will help you to download your Favorite Youtube Videos to an MP4 File
# Before Running the program just make sure that you have the yt_dlp module
# You can install it with this command in the console 
# pip install yt-dlp

# Imports ----------------------------------------------------------------------------------------------

import yt_dlp
import tkinter as tk
from tkinter import Frame, Label, Button, Entry

#Main Function ------------------------------------------------------------------------------------------

def main():
    try:
        print("Code Running Succesfully")
        root = tk.Tk()
        frm_main = Frame(root)
        frm_main.master.title("Bailey")
        frm_main.pack(padx=100, pady=20, fill=tk.BOTH, expand=9)
        populate_main_window(frm_main)
        root.mainloop()
    except Exception as error: 
        print("Something went Wrong :(")
        print(error)
    

## Only for testing, making sure that the function inside of populate_main_window is working properly returning the right URL
def get_video_url(ent_url):
    try:
        url = ent_url.get()
        if url:
            return url
        else: 
            return "Something went Wrong"
    except Exception as e:
        print(e)

# This Function converts the Youtube Link to an MP4 File -----------------------------------------------------
def video_downloader(url):
    try: 
        ydl_opts = {
            'outtmpl': '~/Downloads/Bailey/%(title)s.%(ext)s' 
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return "Download Succesfully :), you will find it in your Downloads File"
    except Exception as e:
        return "Something Went Wrong :("


# This Function Creates the main Screen of the program -----------------------------------------------------
def populate_main_window(frm_main):
    lbl_text = Label(frm_main, text="Please enter the url: ")
    ent_url = Entry(frm_main, width=100)
    btn_dld = Button(frm_main, text="Convert", command=lambda: get_video_url(ent_url))
    lbl_status = Label(frm_main, text="", fg="green")

    # Grid ------------------------------------------------------------------------------------------------- 
    lbl_text.grid(   row=0, column=0, padx=3, pady=3)
    ent_url.grid(   row=0, column=1, padx=3, pady=3)
    btn_dld.grid(   row=0, column=2, padx=3, pady=3)
    lbl_status.grid(   row=1, column=0, columnspan=3, padx=3, pady=3)


    # This Function gets the URL from the user to use it in the video_downloader function------------------
    def get_video_url(ent_url):
        try:
            url = ent_url.get()
            if url:
                message = video_downloader(url)
                lbl_status.config(text=message, fg="green" if "Succesfull" in message else "red")
            else: 
                lbl_status.config(fg="red")
        except Exception as e:
            print(e)

#---------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
 main()