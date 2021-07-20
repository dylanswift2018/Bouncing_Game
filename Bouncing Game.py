#necessary libraries 
from tkinter import *
import time
import random

#creating the opening stage of the game 
stage=Tk()
stage.title("Bouncing Ball Game")
stage.geometry("500x570")
photo = PhotoImage(file = "icon.png")
stage.iconphoto(False, photo)
stage.mainloop()
