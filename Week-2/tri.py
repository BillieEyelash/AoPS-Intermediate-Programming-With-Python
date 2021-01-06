# takes a while!
import turtle

def sierpinski(t,size,depth):
    '''sierpinski(t,size,depth) -> None
    uses turtle t to draw a sierpinski triangle
    size is the overall side length
    depth is the depth
    '''
    # base case
    if depth == 0:
        # draw an equilateral triangle
        for i in range(3):
            t.forward(size)
            t.left(120)

    else:  # recursive step
        # draw first smaller one in lower-left (current position)
        sierpinski(t,size/2,depth-1)

        # move into position and draw 2nd smaller one in lower-right
        t.forward(size/2)
        sierpinski(t,size/2,depth-1)

        # move into position and draw 3rd smaller one on top
        t.left(120)
        t.forward(size/2)
        t.right(120)
        sierpinski(t,size/2,depth-1)

        # move back to starting position
        t.left(60)
        t.back(size/2)
        t.right(60)

# set up turtle and draw
wn = turtle.Screen()
t = turtle.Turtle()
t.ht() # hide turtle so it looks pretty
t.speed(0) # make go fast
# give enough room
t.penup()
t.goto(-200,-200)
t.pendown()
# draw
sierpinski(t,400,6)
wn.mainloop()
