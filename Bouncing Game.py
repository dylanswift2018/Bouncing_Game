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

#creating the Ball model cause we have a lot of balls here 
# object ball :) 
class Ball:
    #constructor
    def __init__(self,cvs,clr,pole,stones,scre):
        self.cvs=cvs
        self.pole=pole
        self.scre=scre
        self.bottom_hit=False
        self.hit=0
        self.id=canvas.create_oval(10,10,25,25,fill=clr,width=1)
        self.cvs.move(self.id,230,461)
        start=[4 ,3.8 ,3.6 ,3.4 ,3.2 ,3 ,2.8 , 2.6 ]
        random.shuffle(start)
        self.a=start[0]
        self.b=-start[0]
        self.cvs.move(self.id,self.a,self.b)
        self.cvs_height=canvas.winfo_height()
        self.cvs_width=canvas.winfo_width()
#when the ball hits another the score gets incremented 
# and we delete the ball after the hit  
    def stone_strike(self,push):
        for line in self.stones:
            for ball in line :
                ball_push=self.cvs.coords(ball.id)

                try:
                    if push[2]>=ball_push[0] and push[0]<= ball_push[2]:
                        if push[3]>= ball_push[1] and push[1]<= ball_push[3]:
                            canvas.bell()
                            self.hit+=1
                            self.scre.configure(text="Score :"+str(self.hit))
                            self.cvs.delete(ball.id)
                            return True
                except:
                    continue
        return False


