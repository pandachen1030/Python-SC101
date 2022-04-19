from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    pre-condition:Karel is on street 1, Avenue 1, facing east
    post-condition:Karel is on beeper and on street 1, Avenue 3, facing South
    """
    while front_is_clear():
        move1()
        turn_left()
        move1()
        move1()
        if front_is_clear():
            turn_right()
        else:
            turn_around()
            going()
    put_beeper()


def move1():
    """
    確保小 karel 不會撞牆
    """
    if front_is_clear():
        move()


def turn_around():
    turn_left()
    turn_left()


def going():
    """
    確保小 karel 不會撞牆
    """
    while front_is_clear():
        move()



def turn_right():
    turn_left()
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
