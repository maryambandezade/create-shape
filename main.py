# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Shape Drawing")

# Create a turtle named "pen"
pen = turtle.Turtle()

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

# Function to draw a triangle
def draw_triangle(size):
    for _ in range(3):
        pen.forward(size)
        pen.right(120)

# Draw a square
pen.color("blue")
draw_square(100)  # Size of the square

# Move the pen to a new location
pen.penup()  # Don't draw while moving
pen.goto(-150, 0)  # Move to the left
pen.pendown()  # Start drawing again

# Draw a triangle
pen.color("green")
draw_triangle(100)  # Size of the triangle

# Finish drawing
pen.hideturtle()  # Hide the turtle
screen.mainloop()  # Keep the window open
