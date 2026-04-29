import turtle
from itertools import cycle

# Step 2: create colors list
colors = ['red', 'green', 'blue', 'yellow', 'magenta']

# Step 3: create cycle for colors
colors = cycle(colors)

# Step 4: create turtle object
t = turtle.Turtle()

# Step 5: set speed of drawing
t.speed(0)

# Step 6: repeat steps
for _ in range(37):
    t.color(next(colors))   # sets the color
    t.circle(50)           # draw a circle with radius 50
    t.left(20)             # move 20 degrees left

turtle.done()
