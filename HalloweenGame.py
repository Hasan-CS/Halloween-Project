# imports
import turtle as trtl
import random as r

reset = trtl.Turtle()
t = trtl.Turtle()
t_two = trtl.Turtle()
counter = trtl.Turtle()
timekeeper = trtl.Turtle()

# variables and other
t.speed(10)
t.penup()
t_two.speed(10)
t_two.penup()
reset.penup()

score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   
timer_up = False
play = True

# placing an image onto the turtles and other initial stuff
wn = trtl.Screen()
wn.bgpic("haunted_house.png")

fd_amount = [200, 100, 75, 50, 25, 10]
angles = [0, 45, 90, 135, 180, 225, 270, 315]
gifs = ["candy.gif", "ghost.gif", "pumpkin.gif", "witch_hat.gif", "bat.gif"]

image = r.choice(gifs)
also_image = r.choice(gifs)
wn.addshape(image)
wn.addshape(also_image)
t.shape(image)
t_two.shape(also_image)

# reset button
reset.speed(0)
reset.goto(340, 205)
reset.color("yellow")
reset.shape("circle")
reset.shapesize(3)

# score writer
counter.penup()
counter.hideturtle()
counter.color("white")
counter.goto(-400, 185)

# time keeper
timekeeper.penup()
timekeeper.hideturtle()
timekeeper.color("white")
timekeeper.goto(-250, 185)

# functions
def move_one():
    randX = r.randint(-200, 200) 
    randY = r.randint(-200, 200) 
    t.goto(randX, randY)

def move_two():
    randX = r.randint(-200, 200) 
    randY = r.randint(-200, 200) 
    t.goto(randX, randY)
    t_two.goto(randX, randY)

def update_score_one(x,y):
    global score 
    global play
    if play == True:
        score += 1
        counter.clear()
        counter.write("Score: " + str(score),font=font_setup)
        move_one()

def update_score_two(x,y):
    global score
    global play
    if play == True: 
        score += 1
        counter.clear()
        counter.write("Score: " + str(score),font=font_setup)
        move_two()

def return_to_origin(x, y):
    t.goto(0, 0)
    t_two.goto(0, 0)

def time_limit():
  global timer, timer_up
  global play
  timekeeper.clear()
  timekeeper.hideturtle()
  if timer <= 0:
    timekeeper.write("Time's Up", font=font_setup)
    timer_up = True
    play = False
  else:
    timekeeper.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    timekeeper.getscreen().ontimer(time_limit, counter_interval)

# gameplay
time_limit()
while play == True:
    t.setheading(r.choice(angles))
    t_two.setheading(r.choice(angles))

    t.fd(r.choice(fd_amount))
    t_two.fd(r.choice(fd_amount))

    t.onclick(update_score_one)
    t_two.onclick(update_score_two)

    reset.onclick(return_to_origin)

wn.mainloop()