screen_precision = 0
console_precision = 0
myVariable = 0
spaces_to_move = 0
dice1 = 0
dice2 = 0
curren_space_numbers = 0
move_forward = Event()
right_turn = Event()
left_turn = Event()

def play_game():
    global myVariable, spaces_to_move, dice1, dice2, curren_space_numbers, move_forward, my_event, right_turn, left_turn, screen_precision, console_precision
    while True:
        roll_dice()
        move()
        complete_task()
        wait(5, MSEC)

def move():
    global myVariable, spaces_to_move, dice1, dice2, curren_space_numbers, move_forward, my_event, right_turn, left_turn, screen_precision, console_precision
    print("VEXcode", end="")
    dice1 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice1))
    brain.screen.next_row()
    dice2 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice2))
    brain.screen.next_row()
    spaces_to_move = dice1 + dice2

def roll_dice():
    global myVariable, spaces_to_move, dice1, dice2, curren_space_numbers, move_forward, my_event, right_turn, left_turn, screen_precision, console_precision
    dice1 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice1))
    brain.screen.next_row()
    dice2 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice2))
    brain.screen.next_row()
    spaces_to_move = dice1 + dice2

def complete_task():
    global myVariable, spaces_to_move, dice1, dice2, curren_space_numbers, move_forward, my_event, right_turn, left_turn, screen_precision, console_precision
    brain.screen.print(str("Landed on space") + str(curren_space_numbers))
    brain.screen.next_row()
    wait(1, SECONDS)
    if curren_space_numbers == 1:
        # Space = GO
        pass
    elif curren_space_numbers == 4:
        # Space = Jail
        pass
    elif curren_space_numbers == 7:
        # Space = Free Parking
        pass
    elif curren_space_numbers == 10:
        # Space = Go to Jail
        pass
    else:
        # Space + Blue 1 or 2, Green 1 or 2, Yellow 1 or 2, or Red 1 or 2
        pass
    if curren_space_numbers == 1:
        # Space = GO
        for repeat_count2 in range(4):
            left_turn.broadcast_and_wait()
            wait(5, MSEC)
    elif curren_space_numbers == 4:
        # Space = Jail
        wait(3, SECONDS)
    elif curren_space_numbers == 7:
        # Space = Free Parking
        wait(5, SECONDS)
    elif curren_space_numbers == 7:
        # Space = Go to Jail
        right_turn.broadcast_and_wait()
        for repeat_count3 in range(3):
            move_forward.broadcast_and_wait()
            wait(5, MSEC)
        left_turn.broadcast_and_wait()
        for repeat_count4 in range(3):
            move_forward.broadcast_and_wait()
            wait(5, MSEC)
        for repeat_count5 in range(2):
            right_turn.broadcast_and_wait()
            wait(5, MSEC)
        curren_space_numbers = 4
        wait(1, SECONDS)
    else:
        # Space + Blue 1 or 2, Green 1 or 2, Yellow 1 or 2, or Red 1 or 2
        right_turn.broadcast_and_wait()
        move_forward.broadcast_and_wait()
        for repeat_count6 in range(2):
            left_turn.broadcast_and_wait()
            wait(5, MSEC)
        move_forward.broadcast_and_wait()
        right_turn.broadcast_and_wait()

def when_started1():
    global myVariable, spaces_to_move, dice1, dice2, curren_space_numbers, move_forward, my_event, right_turn, left_turn, screen_precision, console_precision
    spaces_to_move = 1
    play_game()

when_started1()

