from turtle import Turtle, Screen
screen = Screen()

DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):

        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for pixel in range(0, 3):
            snake_piece = Turtle()
            snake_piece.shape("square")
            snake_piece.penup()
            snake_piece.color("white")
            snake_piece.goto(y=0, x=-DISTANCE*pixel)
            self.snake.append(snake_piece)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def move(self):
        screen.listen()
        screen.onkeypress(key="Up", fun=self.up)
        screen.onkeypress(key="Down", fun=self.down)
        screen.onkeypress(key="Left", fun=self.left)
        screen.onkeypress(key="Right", fun=self.right)

        for seg in range(len(self.snake)-1, 0, -1):
            self.snake[seg].goto(self.snake[seg - 1].pos())

        self.head.forward(DISTANCE)
