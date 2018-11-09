from tkinter import *
import cv2
import os

def digitalcam9():
	os.system("gnome-terminal -e 'bash -c \"python cam9.py; exec bash\"'")

def digitalcam10():
	os.system("gnome-terminal -e 'bash -c \"python cam10.py; exec bash\"'")


def analogcams():
	os.system("gnome-terminal -e 'bash -c \"python analogcams.py; exec bash\"'")


a = Tk()
a.title("MRM") 																																											
Button(a, text="DigitalCam9", command = digitalcam9, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 0)
Button(a, text="DigitalCam10", command = digitalcam10, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 1)
Button(a, text="AnalogCams", command = analogcams, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 4)



def motorcode():
	os.system("gnome-terminal -e 'bash -c \"python udp.py; exec bash\"'")
	
Button(a, text="Motorcode", command = motorcode, bg="white", fg="black",font=("comic_sans",15,"bold")).grid(row = 0,column=2)

def autonomous():
	 os.system("gnome-terminal -e 'bash -c \"sudo python autnomRec.py; exec bash\"'")


Button(a, text="Autonomous", command = autonomous, bg="white", fg="black",font=("comic_sans",15,"bold")).grid(row = 0,column=3)

a.mainloop()
