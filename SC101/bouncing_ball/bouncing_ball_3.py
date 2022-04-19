"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
LIFE = 3

window = GWindow(800, 500, title='bouncing_ball.py')
count = 1
switch = True  #開關
ball = GOval(SIZE, SIZE)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, START_X, START_Y)
    onmouseclicked(bounce)


def bounce(click):
    global count, switch
    ball_y = 1  # 球向下墜的速度，假設初始值為 1
    if switch and count <= 3:  # 必須開關打開且次數小於等於3才會執行
        switch = False
        while True:
            ball.move(VX, ball_y)  # 球向右下墜的速度，並且有一個重力加速度
            ball_y += GRAVITY
            if ball.y + ball.height >= window.height:
                ball_y = -ball_y * REDUCE
            if ball.x - ball.width >= window.width:
                switch = True
                break
            pause(DELAY)
        window.add(ball, x=START_X, y=START_Y)
        count += 1


if __name__ == "__main__":
    main()
