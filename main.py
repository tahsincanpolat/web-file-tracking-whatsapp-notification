import pywhatkit
import datetime
import time
import requests
import pywhatkit
from dateutil.parser import parse as parsedate
from tkinter import *

def run():
    r = requests.head(link.get())
    url_time = r.headers['last-modified']
    url_date = parsedate(url_time)
    while True:
        r = requests.head(link.get())
        url_time = r.headers['last-modified'] #web file last-modified time 
        url_change_date=parsedate(url_time)
        if url_date==url_change_date:
            print("Not changed")
            time.sleep(1)
        else:
            print("Changed")
            an = datetime.datetime.now()
            dakika=an.minute+1
            saat=an.hour
            pywhatkit.sendwhatmsg(tel.get(),"Warning. File is changed. ",saat,dakika) #Use web.whatsapp to use pywhatkit
            time.sleep(60)
            break

window = Tk()
window.geometry("400x400")
window.title("Whatsapp Notification Web File Tracking")
tel=Entry()
link=Entry()
tel_label = Label(text="Phone: ") 
link_label = Label(text="Link: ") 
tel_label.pack()
tel.pack()
link_label.pack()
link.pack()
dugme = Button(text="Turn On Natification!",command=run)
dugme.pack()

mainloop()



