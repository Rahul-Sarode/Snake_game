from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.snake_objects = []
        self.create_snake()
        self.snake_head = self.snake_objects[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_objects.append(new_segment)

    def reset(self):
        for seg in self.snake_objects:
            seg.goto(1000, 1000)
        self.snake_objects.clear()
        self.create_snake()
        self.snake_head = self.snake_objects[0]

    def extend(self):
        self.add_segment(self.snake_objects[-1].position())

    def snake_movement(self):
        for segment_num in range(len(self.snake_objects) - 1, 0, -1):
            new_x = self.snake_objects[segment_num - 1].xcor()
            new_y = self.snake_objects[segment_num - 1].ycor()
            self.snake_objects[segment_num].goto(new_x, new_y)
        self.snake_head.forward(20)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(RIGHT)

