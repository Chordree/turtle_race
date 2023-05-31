import turtle, time, random

width, height = 800, 700
colours = ['red', 'yellow', 'grey', 'green', 'blue', 'orangered', 'cyan', 'magenta',
           'black', 'indigo', 'pink', 'brown']


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


# add the other block that can handle number of racers # and comment one

def race_screen():
    display = turtle.Screen()
    display.title('Race Track')
    display.setup(width, height)


def racers(colour_list):
    icons = []
    for i, color in enumerate(colour_list):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        spacer = width / (len(colour_list) + 1)
        racer.setpos((-width / 2) + spacer * (i+1), (-height / 2) + 20)
        # the below would also work fine with >> spacer = width / (len(colour_list)) # not evenly spaced with the win
        # racer.setpos((-width / 2) + 20 + spacer*i, (-height / 2) + 20)
        racer.pendown()
        icons.append(racer)
    return icons

#  racing function .. see to draw race track also # based on num of users


# make the below into a function
num_racers = enter_num_racers()
race_screen()
random.shuffle(colours)
colors = colours[:num_racers]
print(colors)  # not really necessary
cars = racers(colors)


# add a function that would allow user choose colour and assign random on not choosing
def main():
    while True:
        for car in cars:
            sp = random.randrange(5, 8)  # see if this speed is necessary ... check the effect
            dst = random.randrange(5, 16)  # you can also make this values dynamic based on height
            car.speed(sp)
            car.forward(dst)
            if car.pos()[1] >= height / 2 - 10:     # .pos(): returns the x, y coordinate
                print(car.pos())
                print(f'the winner is {car.color()}')
                return f'the winner is {car.color()}'
                # see to use .index method in tms version



main()

# Todo:
# make this a shape race later on, check how random.shuffle works,
# allow users to use choose colours in another version
# draw the track lines and finish line also
# checkout the game blasters



# this are just some sample turtle movement demo

# racer = turtle.Turtle()
# racer.speed(1)
# racer.shape('turtle')
# racer.color(colors[1])
# racer.forward(350)
# racer.penup()
# racer.left(90)
# racer.forward(150)
# racer.left(100)
# racer.pendown()
# racer.backward(-200)
# time.sleep(5)