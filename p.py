import turtle

bob = turtle.Turtle()

def square(side):
    for i in range(4):
        bob.forward(side)
        bob.left(90)

square(200)
turtle.mainloop()
