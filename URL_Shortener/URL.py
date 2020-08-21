import pyshorteners
import tkinter as tk
from tkinter import *

def shortt():
	global temp_s
	global temp_p
	global temp_d
	

	try:
		s=temp_s.get()
		temp_d=(pyshorteners.Shortener())
		temp_p.set(temp_d.tinyurl.short(s))
	except:
		pass

root = tk.Tk()
root.geometry('371x108')
root.config(bg="orange")
root.title("URL Shortener")


temp_s = tk.StringVar()
temp_p = tk.StringVar()

f=Frame(root)
f.grid()


f1 = Frame(root)
f1.grid()
Label(f1,text='Enter link here-->',font=5).grid(row=1)
Entry(f1,font=5,textvariable=temp_s,bg="black",foreground="orange").grid(row=1,column=1,pady=5,padx=10)
Label(f1,text='Your Shorten URL is-->',font=5).grid(row=2)
Entry(f1,textvariable=temp_p,font=5,bg="black",foreground="orange").grid(row=2,column=1)
Button(f1,text='Shorten',padx=50,relief=RAISED,font=10,borderwidth=5,command=shortt,bg="black",foreground="Orange").grid(row=3,column=1,pady=5)

root.mainloop()