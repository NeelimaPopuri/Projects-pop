import turtle


WIDTH, HEIGHT = 500, 500


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers?(2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is invalid Number")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Numbers not in a range 2-10.. Try Again....")


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles .append(racer)


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")


racers = get_number_of_racers()
init_turtle()
