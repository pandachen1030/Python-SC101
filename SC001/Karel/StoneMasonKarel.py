from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    pre-condition:Karel is on street 1, Avenue 1, facing east
    post-condition:Karel is on beeper and on street 1, Avenue 13, facing east
    """
    while front_is_clear():
        circle()


def circle():
    """
    以填滿兩個柱子為單位，做一個循環，讓小 karel 可以填滿柱子
    """
    turn_left()
    while front_is_clear():
        put()
    if not on_beeper():
        put_beeper()
    turn_right()
    move4()
    turn_right()
    while front_is_clear():
        put()
    turn_left()
    if front_is_clear():
        move4()


def turn_right():
    for i in range(3):
        turn_left()


def move4():
    """
    移動到下一根柱子
    """
    for i in range(4):
        move()


def put():
    """
    確保最後一格有放到 beeper
    """
    if not on_beeper():
        put_beeper()
    move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
