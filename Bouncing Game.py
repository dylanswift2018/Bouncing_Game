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
stage.resizable(0,0)
stage.wm_attributes("-topmost",1)
#the game zone 
canvas= Canvas(stage,width=500,height=500,bd=0,highlightthickness=0,highlightbackground="Red",bg="White")
canvas.pack(padx=10,pady=10)
#the scoring zone to display it to the player 
score= Label(height=50,width=80,text="Score : 0",font="Calibri 16 bold")
score.pack(side="left")
stage.update()

