import turtle
from tkinter import *
import tkinter as tk


class Snowflake:
     
     #Constructor which creates the tk canvas for the turtle and widgets to be added onto the screen
       
    def __init__(self, master):
        
        self.master = master
        self.master.title("Koch Snowflake")
        self.frameOne()
        self.frameTwo()
        
        
        self.master.bind("<Configure>", lambda e: self.press(e))
    
    #Method which sets up first frame for slider and button to go on   
    def frameOne(self):
        self.frame1 = tk.Frame(self.master)
        self.frame1.pack(side = tk.RIGHT)
        
        #slider
        self.slider = Scale(self.frame1, from_=1, to=12, orient=HORIZONTAL)
        self.slider.pack()
        
        #button
        self.my_btn = tk.Button(self.frame1, text="Click me to go to this order")
        self.my_btn.bind('<Button>', lambda e : self.press(e))
        self.my_btn.pack()
     
    #Method which sets up second frame for the canvas and screen to be added onto to draw the snowflake   
    def frameTwo (self):
        self.frame2 = tk.Frame(self.master)
        self.frame2.pack(fill = tk.BOTH, expand = tk.YES, side = tk.LEFT)
        
        #canvas
        self.canvas = tk.Canvas(self.frame2, width= 700, height= 500)
        self.canvas.pack(fill=tk.BOTH, expand = tk.YES)
        
        #screen
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("pink")
        self.t = turtle.RawTurtle(self.screen)
        self.t.hideturtle()
        self.screen.tracer(0,0)
    
        
        
        
    # Recursive method which draws one side of the snowflake
    def koch(self, length, step):
        if(step == 0): 
            self.t.forward(length)
        else:
            length = length / 3.0
            step = step -1 
            self.koch(length, step)
            self.t.right(60)
            self.koch(length, step)
            self.t.left(120)
            self.koch(length, step)
            self.t.right(60)
            self.koch(length, step)
        
            
         
    # Method whichdraws the full snowflake and calls koch method for recursion
    def fullSnowflake(self, x, length):   
        for index in range(3): 
            self.koch(length, x)
            self.t.left(120)
        self.screen.update()
        
   
    # Method which gets input from slider wigit and calls fullSnowflake    
    def press(self, e):
        
        self.t.clear()
        x = self.slider.get() -1
        
        #get width and height
        swidth = self.master.winfo_width()
        sheight = self.master.winfo_height()
        length = (swidth + sheight) / 6.0
        
        #change origin 
        self.t.penup()
        self.t.goto(-200 + self.frame2.winfo_width() /3 ,-150)
        self.t.pendown()
     

        self.fullSnowflake(x,length)
        self.screen.update()
            
            

# Main method which initizlises and calls the class to run    
if __name__ == "__main__":
    root = tk.Tk()
    snowflake = Snowflake(root)
    root.mainloop()