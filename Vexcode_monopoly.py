screen_precision = 0
console_precision = 0
myVariable = 0
current_space_number = 0
dice1 = 0
dice2 = 0

def play_game():
    global myVariable, current_space_number, dice1, dice2, screen_precision, console_precision
    while True:
        roll_dice()
        move()
        complete_task()
        wait(5, MSEC)

def move():
    global myVariable, current_space_number, dice1, dice2, screen_precision, console_precision
    pass

def complete_task():
    global myVariable, current_space_number, dice1, dice2, screen_precision, console_precision
    pass

def roll_dice():
    global myVariable, current_space_number, dice1, dice2, screen_precision, console_precision
    pass

def when_started1():
    global myVariable, current_space_number, dice1, dice2, screen_precision, console_precision
    current_space_number = 1
    play_game()

when_started1()
