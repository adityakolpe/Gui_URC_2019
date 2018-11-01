from tkinter import *
import cv2
import os

def cam1():
	os.system("gnome-terminal -e 'bash -c \"python cam1.py; exec bash\"'")


a = Tk()
a.title("MRM") 																																											
Button(a, text="Camera Feed1", command = cam1, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 0)


def motorcode():
	os.system("gnome-terminal -e 'bash -c \"python udp.py; exec bash\"'")
	
Button(a, text="Motorcode", command = motorcode, bg="white", fg="black",font=("comic_sans",15,"bold")).grid(row = 0,column=1)

def gpsplotting():
	 os.system("gnome-terminal -e 'bash -c \"python map1.py; exec bash\"'")


Button(a, text="gpsplotting", command = gpsplotting, bg="white", fg="black",font=("comic_sans",15,"bold")).grid(row = 0,column=2)

a.mainloop()
