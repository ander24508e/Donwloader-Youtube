import yt_dlp as youtube_dl
from tkinter import *
from tkinter import filedialog
import os

def select_folder():
    folder_selected = filedialog.askdirectory()
    return folder_selected

def Downloader():
    url = link.get()
    save_path = select_folder()
    if not save_path:
        Label(root, text='Por favor, seleccione una carpeta',
              font='arial 13 bold', bg='black', fg='white').pack()
        return

    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),  # Guarda con el nombre del video en la carpeta seleccionada
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    Label(root, text='Descarga finalizada', font='arial 13 bold',
          bg='black', fg='white').pack()

root = Tk()
root.geometry('500x400')
root.resizable(0, 0)
root.title('Ander Downloader')
root.configure(bg='black')

Label(root, text='Download Video', font='arial 20 bold', bg='black', fg='white').pack(pady=20)
link = StringVar()
Label(root, text='Link del video:', font='arial 12', bg='black', fg='white').pack(pady=10)
Entry(root, width=50, textvariable=link).pack(pady=5)

Button(root, text='DESCARGAR', font='arial 13 bold italic', bg='white', fg='black',
       padx=2, command=Downloader).pack(pady=20)

root.mainloop()