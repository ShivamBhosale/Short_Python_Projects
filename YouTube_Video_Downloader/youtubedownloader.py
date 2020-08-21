import os
from tkinter import *

root = Tk()
root.geometry('328x82')
root.config(bg="orange")
root.title("YouTube Video Downloader")
def runit():
	os.startfile('link.bat')
def downloadytv():
	with open('link.bat','w') as down_load:
		down_load.write(f'youtube-dl {link.get()}')
		down_load.close()
	runit()
f =Frame(root)
f.grid()


f1 = Frame(root)
f1.grid()
Label(f1,text='Enter link here-->',font=5,bg="light blue").grid(row=1)

link = StringVar()

Entry(f1,font=5,textvariable=link,bg="light blue").grid(row=1,column=1,pady=5,padx=10)

Button(f1,text='Download',padx=50,relief=RAISED,font=10,borderwidth=5,command=downloadytv,bg="light blue").grid(column=1,pady=5)


root.mainloop()
