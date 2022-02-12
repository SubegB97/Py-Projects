import turtle 

#Creates the Window
wn = turtle.Screen()
#Title of the game
wn.title("Python Classic Pong by Baz")
#Background color of the window
wn.bgcolor("blue")
#Size of the window
wn.setup(width=800, height=600)
#Speeds up the game
wn.tracer(0)

#Score
score_a = 0
score_b = 0

# Paddle A
#paddle a is a turtle object, small t is the module name, big T since its a class
paddle_a = turtle.Turtle()
#speed of animation, sets it to maximum possible speed
paddle_a.speed(0)
#paddle shape
paddle_a.shape("square")
#paddle color
paddle_a.color("pink")
#paddle width and length 
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
#Turtle by defintion draws line when moving, we do not need to draw a line. 
paddle_a.penup()
#Paddle location on the console 
paddle_a.goto(-350, 0)

# Paddle B 
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("pink")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
#Swapped location to +350
paddle_b.goto(350, 0)

#Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
#delta or change, everytime the ball moves, it moves by 2 pixels. Since x is positive it'll move right 2 and since y is positive
# it'll move up 2 or diagonally 
ball.dx = .5
ball.dy = -.5

# Pen - turtle module gives the turltes a lot of abilities
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
#hides the pen, just want to see the written text
pen.hideturtle 
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))



#Funciton (a piece of a program that does something that has been defined for it)
#define function first
def paddle_a_up():
    #Need to know current y coordinate, .ycore is from turtle module, returns y coordinate
    y = paddle_a.ycor()
    #This will add 20 pixels to y coordinate 
    y += 20 
    #paddle a is now set to the y variable 
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)
#Keyboard binding 
#Listen module tells the program to listen for keyboard input 
wn.listen()
#When user presses "W" on keyboard, call the function paddle_a_up
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

# Main game loop 
#While loop where everytime the loop runs, it updates 
while True:
    wn.update()

    # Move the ball with current x coordinate, ball starts at 0,0 then it'll go 2, 2, 2,....
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking Top and Bottom
    # if statment, if the y coordinate of the ball is greater than 290
    if ball.ycor() > 290:
        # set the ball back to 290
        ball.sety(290)
        # reverses the direction since dy is .5 it'll now be -.5
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 

    # Border Checking Left and Right
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        #increments and adds one every time the ball goes off the screen on the right side for player a 
        score_a += 1
        #Clears the screen
        pen.clear()
        #Displays printed score with .format module will update the score every time a player scores
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1 
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions 
    # If the x coordinate of the ball is greater than 340 and is it between top of the paddle and bottom of the paddle?
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
