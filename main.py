import turtle

drawing_board=turtle.Screen()
drawing_board.bgcolor("lightblue")
drawing_board.title("Simple Turtle")

turtle_instance=turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("red")

def turtle_forward():
    turtle_instance.forward(100)
def rotate_left():
    turtle_instance.left(90)
def rotate_right():
    turtle_instance.right(90)

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key= "space")
drawing_board.onkey(fun=rotate_right,key= "Right")
drawing_board.onkey(fun=rotate_left,key= "Left")

turtle.mainloop()