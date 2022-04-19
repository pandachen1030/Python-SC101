from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""


def main():
    """
    pre-condition:Karel is on street 1, Avenue 1, facing east
    post-condition:Karel is on street 8, Avenue 1, facing North
    """
    put_beeper()
    while front_is_clear():
        circle()
    while not front_is_clear():
        """
        避免 1x1 的世界動不了
        """
        if facing_east():
            turn_left()
            circle()


def circle():
    """
    填滿一行以後進到下一行去填滿，以兩行為一個循環
    """
    fill_1_line()
    turn_left()
    if front_is_clear():
        """
        避免遇到奇數行的世界
        """
        move()
        check_back()
        turn_left()
        fill_1_line()
        turn_right()
        if front_is_clear():
            move()
            check_back()
            turn_right()


def turn_right():
    for i in range(3):
        turn_left()


def fill_1_line():
    """
    間隔放 beeper 填滿一行
    """
    while front_is_clear():
        move()
        check_back()


def check_back():
    """
    確認後面的格子是否有 beeper，有的話就前進；反之放beeper
    """
    turn_around()
    move()
    if not on_beeper():
        turn_around()
        move()
        put_beeper()
    else:
        turn_around()
        move()


def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
