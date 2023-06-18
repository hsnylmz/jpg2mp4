import os
import subprocess
import datetime

from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from tkinter import filedialog, Tk, Button

window = ttk.Window(title="raw2mp4 by hsnylmz", themename="darkly")
window.geometry("300x80")
window.resizable(False,False)

try:
    window.iconbitmap('icon.ico')
except:
    pass

videos_folder = os.path.join(os.path.expanduser("~"), "Videos")
create_video_folder = os.path.join(videos_folder, "Raw_Convert")

try:
    os.mkdir(create_video_folder)   
except:
    pass

def cevir():
    yol=os.getcwd()
    os.chdir(yol)
    # video adı için 
    simdi = datetime.datetime.now()
    saat = simdi.hour
    dakika = simdi.minute
    saniye = simdi.second
    yil = simdi.year
    ay = simdi.month
    gun = simdi.day
    video_folder= str(yil) + '_' +str(ay) + '_' + str(gun) + '_' + str(saat) + '_' + str(dakika) + '_' + str(saniye)
    video_adi= str(yil) + '_' +str(ay) + '_' + str(gun) + '_' + str(saat) + '_' + str(dakika) + '_' + str(saniye)+'.mp4'

    create_video_folder_session = os.path.join(create_video_folder, video_folder)

    try:
        os.mkdir(create_video_folder_session)
    except:
        pass
    
    source_dir = filedialog.askdirectory(initialdir=videos_folder)
    
    #os.system('python arwjpg.py -s '+ source_dir +' -t destination_dir')
    command = 'python arwjpg.py -s "{}" -t "{}"'.format(source_dir, create_video_folder_session)
    
    os.system(command)

    yolumuz=os.getcwd()
    convert_command='{}/ffmpeg.exe -framerate 24 -i {}/image%05d.JPG {}/{}'.format(yolumuz, create_video_folder_session,create_video_folder,video_adi)
    #print(convert_command)
    os.system(convert_command)

    #biten klasörü aç
    subprocess.call('explorer ' + create_video_folder + ', shell=True')
    
    #biten videoyu aç
    os.chdir(create_video_folder)
    subprocess.Popen([video_adi], shell=True)
    convert_button.config(state=DISABLED, text="Y E N İ D E N   B A Ş L A T I N I Z", cursor='question_arrow')
 
#buttonlar
convert_button = ttk.Button(window, text="K L A S Ö R   S E Ç İ N İ Z", command=cevir, width=50, bootstyle=SUCCESS)
convert_button.pack(side='left', padx=5, pady=5)

window.mainloop()
