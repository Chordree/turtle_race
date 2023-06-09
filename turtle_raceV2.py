import random
import time
import turtle

# make this a shape race later on .. see shapes_race in this repo
# allow users to use choose colours in another version


width, height = 800, 700
colours = ['red', 'yellow', 'grey', 'green', 'blue', 'orange', 'cyan', 'magenta',
           'black', 'indigo', 'pink', 'brown']


def enter_num_racers():
    while True:
        val = (input('enter number of races: '))
        if val.isdigit():
            val = int(val)
            if val not in range(3, 13):
                print('pls enter a val btw 3 and 12')
                continue
            return val
        else:
            print("pls enter a number ")


def race_screen():
    display = turtle.Screen()
    display.title('Turtle race with tracklines')
    display.setup(width, height)


# try the commented  racer.setpos() below to see how it would arrange the racers 
def racers(colour_list):
    icons = []
    for i, color in enumerate(colour_list):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        spacer = width / (len(colour_list) + 1)
        racer.setpos((-width / 2) + spacer * (i + 1), (-height / 2) + 20)
        # the below would also work fine with >> spacer = width / (len(colour_list)) # not evenly spaced with the win
        # racer.setpos((-width / 2) + 20 + spacer*i, (-height / 2) + 20)
        # see to use this method for the position cause of track drawing .. vice versa or for the track
        racer.pendown()
        icons.append(racer)
    return icons


def track_lines(val):
    for i in range(val - 1):
        s = width / (val + 1)
        track = turtle.Turtle()
        track.color('orangered')  # you can decide not to add a color .. it would be black by default
        track.left(90)
        track.penup()
        # compare the trackline pattern here with the one in shapes_race in this same repo
        track.setpos((-width / 2) + s/2 + s + s*i, (-height / 2))
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
    race_screen()
    random.shuffle(colours)
    colors = colours[:num_racers]
    print(colors)  # not really necessary, just printing the shuffle function to show you the shuffle effect
    track_lines(num_racers)
    cars = racers(colors)
    while True:
        for car in cars:
            spd = random.randrange(5, 8)  # see if this speed is necessary ... check the effect
            dst = random.randrange(5, 16)  # you can also make this values dynamic based on height
            car.speed(spd)
            car.forward(dst)
            if car.pos()[1] >= height / 2 - 10:  # .pos(): returns the x, y coordinate
                print(car.pos())  # not really important .. just showing the tuple value in the winner coordinate
                print(f'the winner is {car.color()}') # see to use .index method to print winner in a cleaner way
                return f'the champion is {car.color()}'  # this would display output if you call print(main())
                # however the return statement is till important to break the while loop and end the fuction call  
                # not to include return incase you remove the line above as the while loop would keep running 
                


main()
time.sleep(7)  # for the turtle window  to be static for some seconds before closing


