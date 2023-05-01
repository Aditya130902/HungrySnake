from turtle import Turtle
TURTLE_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.turtles = []
        self.snake_creation()

    def snake_creation(self):
        for item in TURTLE_COORDINATES:
            new_turtle = Turtle('square')
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.goto(item)
            self.turtles.append(new_turtle)

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            self.turtles[i].goto(self.turtles[i - 1].xcor(), self.turtles[i - 1].ycor())
        self.turtles[0].forward(20)

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

    def extend_snake(self):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(self.turtles[-1].position())
        self.turtles.append(new_turtle)

    def reset(self):
        for turtle in self.turtles:
            turtle.goto(700, 700)
        self.turtles.clear()
        self.snake_creation()
