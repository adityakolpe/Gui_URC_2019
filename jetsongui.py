#!/usr/bin/python
from Tkinter import *
import cv2
import os
import subprocess
from time import sleep



def map1():
	os.system("idle-python2.7 -r map1.py &")

	proc = subprocess.Popen(["xdotool search --onlyvisible --name MRM"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 0 0 &"
	os.system(cmd)
	sleep(1)
	proc = subprocess.Popen(["xdotool search --onlyvisible --name cam10"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	cmd="xdotool windowmove "+out.strip()+" 100 0 &"
	os.system(cmd)
	sleep(1)
	proc = subprocess.Popen(["xdotool search --onlyvisible --sync --name Python\ 2.7"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	
	#os.system("xdotool search --onlyvisible --sync --name \"Python\ 2.7+\ Shell\" set_window --name \"Motorcode\"")
	for i in out.split():
		os.system("xdotool windowminimize "+i.strip())
a = Tk()
a.title("MRM") 	

Button(a, text="Map", command = map1, bg="white", fg = "black", font=("comic_sans",15,"bold")).grid(row = 0, column = 5)

a.mainloop()