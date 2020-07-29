#Project by Sommaya Haque
#My project is a picture of a snowy scene in the city.

import turtle
import random

def main():
    turtle.speed(100)
    screen=turtle.getscreen()
    screen.bgcolor('navy')
    draw_building(0,-100,20)
    draw_building(-200,-100,20)
    draw_building(200,-100,20)
    draw_ground(1000,-400,'olive')
    draw_tree(-100,80)
    draw_tree(-200,80)
    draw_tree(100,80)
    draw_tree(220,80)
    draw_moon()
    draw_snow()

def draw_square(l,w,c):#draw square function
    turtle.begin_fill()
    turtle.fillcolor(c)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.end_fill()
    
def draw_building(x,y,s):#draw a building function
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    draw_square(150,375,'gray')
    #windows floor 1
    turtle.penup()
    turtle.goto(x+20,y+200)
    turtle.pendown()
    draw_square(100,40,'blue')
    #window floor 2
    turtle.penup()
    turtle.goto(x+20,y+280)
    turtle.pendown()
    draw_square(100,40,'blue')
    

def draw_ground(q,a,c):#draw the ground function
    turtle.penup()
    turtle.goto(-500,0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(c)
    turtle.forward(q)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(q)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.end_fill()

def draw_tree(r,o):#draw a tree function
    #trunk
    turtle.penup() 
    turtle.goto(r-35,o-25)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('brown')
    draw_square(20,-60,'brown')
    #bottom triangle
    turtle.penup()
    turtle.goto(r+10,o-50)
    turtle.pendown()
    turtle.fillcolor('green')
    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(80)
    turtle.left(120)
    turtle.forward(80)
    turtle.left(120)
    turtle.forward(80)
    turtle.end_fill()
    #top triangle
    turtle.penup() 
    turtle.goto(r,o)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(60)
    turtle.left(120)
    turtle.forward(60)
    turtle.left(120)
    turtle.forward(60)
    turtle.end_fill()

def draw_moon(): #draws the moon
    turtle.penup()
    turtle.goto(-400,300)
    turtle.pendown()
    turtle.dot(100,'white')
    turtle.penup()
    turtle.goto(-370,300)
    turtle.pendown()
    turtle.dot(85,'navy')

def draw_snow(): #draws snow
    L= 100 #amount of snowflakes
    count=0
    while L>count: #put snow in random places
        numberx= random.randint(-400,400)
        numbery= random.randint(-400,400)
        turtle.penup()
        turtle.goto(numbery,numberx)
        turtle.pendown()
        turtle.dot(5,'white')
        count=count+1

#call main again
main()
