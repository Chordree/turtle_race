import random
import time
import turtle

width, height = 800, 700
colours = ['red', 'yellow', 'grey', 'green', 'blue', 'orangered', 'cyan', 'magenta',
           'black', 'indigo', 'pink', 'brown']  
# you can add more valid colours/colour names ..see turtle documentation 


def enter_num_racers():
    while True:
        try:
            num = int(input('enter desired number of racers btw(2 - 12): '))
            if num not in range(2, 13):
                print('number must be btw 2 and 12')
                continue
            return num
        except ValueError:
            print("you didn't enter a number")

def enter_shape():
    print('available shapes are  >> triangle, circle, square & turtle ')
    shape = input('enter desired shape: ').strip().lower()
    shapes_list = ['triangle', 'circle', 'square', 'turtle']  # you can add other valid shapes ..see turtle doc
    while shape not in shapes_list:
        print('available shapes are  >> triangle, circle, square & turtle ')
        shape = input('enter desired shape: ').strip().lower()
        # the strip and lower methods are to strip spaces and change the user input to lowercase  
    return shape


def race_screen():
    display = turtle.Screen()
    display.title('Shapes race with tracklines')
    display.setup(width, height)


def racers(colour_list, shp):
    icons = []
    for i, color in enumerate(colour_list):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape(shp)
        racer.left(90)
        racer.penup()  # so the shapes don't draw traces from where they are being created to thier race start marks 
        spacer = width / (len(colour_list) + 1)
        racer.setpos((-width / 2) + spacer * (i + 1), (-height / 2) + 20)
        racer.pendown()
        icons.append(racer)
    return icons


def track_lines(val):
    for i in range(val + 1):
        s = width / (val + 1)  # s is just the spacing btw tracks 
        track = turtle.Turtle()
        track.color('violet')  # you can decide not to add a color .. it would be black by default
        track.left(90)
        track.penup()
        track.setpos((-width / 2) + s/2 + s*i, (-height / 2)) 
        track.pendown()
        track.forward(height + 8)  # the addition is to hide the arrow head of the track lines
    # drawing of finish line .. not really important
    finish_line = turtle.Turtle()
    finish_line.penup()
    finish_line.setpos(-width / 2, height / 2 - 4)
    finish_line.pendown()
    finish_line.color('purple')
    finish_line.forward(width)


def main():
    num_racers = enter_num_racers()
    shape = enter_shape()
    race_screen()
    random.shuffle(colours)
    colors = colours[:num_racers]
    print(colors)  # not really necessary.. just printing the shuffled colours 
    track_lines(num_racers)
    cars = racers(colors, shape)  
    while True:
        for car in cars:
            spd = random.randrange(5, 8)  # see if this speed is necessary ... check the effect
            dst = random.randrange(5, 16)  # you can also make this values dynamic based on height
            car.speed(spd)
            car.forward(dst)
            if car.pos()[1] >= height / 2 - 10:  # .pos(): returns the x, y coordinate
                print(car.pos())  # not really important .. just showing the tuple value in the winner coordinate
                print(f'the winner is {car.color()}')
                # see to use .index method in tms version .. print winer with shape
                return         
                 

main()
time.sleep(7)  # for the turtle window  to be static for some seconds before closing

# Todo : make a upgrade  that allow users to use choose colours in another version,
# input racernames, ... play around features 

