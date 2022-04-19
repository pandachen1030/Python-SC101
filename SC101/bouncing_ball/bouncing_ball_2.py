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

window = GWindow(800, 500, title='bouncing_ball.py')
count = 1
ball = GOval(SIZE, SIZE)

click_status = True
allow_exe = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global click_status, allow_exe, count
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(bounce)


def bounce(click):
    global click_status, allow_exe, count
    vy = GRAVITY
    if count > 3:
        allow_exe = False
        click_status = False
    if click_status:
        allow_exe = True
    if click_status and allow_exe:
        click_status = False
        while allow_exe:
            if ball.x + SIZE >= window.width:
                window.add(ball, START_X, START_Y)
                count += 1
                click_status = True
                allow_exe = False
            elif count <= 3:
                ball.move(VX, vy)
                if ball.y + SIZE >= window.height and vy > 0:
                    vy = -vy*REDUCE
                else:
                    vy += GRAVITY
            pause(DELAY)


if __name__ == "__main__":
    main()
