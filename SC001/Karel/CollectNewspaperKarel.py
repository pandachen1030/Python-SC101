from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: Panda
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    pre-condition:Karel is on street 3, Avenue 6, facing east
    post-condition:Karel is on beeper and on street 3, Avenue 6, facing east
    TODO:讓小 karel 可以找到報紙
    """
    go()
    turn_right()
    find_door()
    turn_left()
    move()
    pick_beeper()
    turn_around()
    go()
    turn_right()
    go()
    turn_right()
    put_beeper()


def go():
    """
    不要讓小 karel 撞牆
    """
    while front_is_clear():
        move()


def find_door():
    """
    到底後可以找到右邊的們在哪
    """
    while not left_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
