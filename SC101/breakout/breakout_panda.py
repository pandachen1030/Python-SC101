"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.ginteractors import GButton
from campy.graphics.gwindow import Region
from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
from campy.gui.events.timer import pause
from breakoutgraphics_panda import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gimage import GImage

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts

start = False


def main():
    graphics = BreakoutGraphics()
    while True:
        if graphics.restart_on:
            graphics.restart_on = False
            lives = NUM_LIVES
            graphics.set_lives(lives)
            graphics.set_heart()
            while True:
                graphics.moving_wall()
                if graphics.switch and graphics.lives > 0:
                    graphics.ball_move()
                if graphics.lives <= 0:
                    graphics.button.enable()
                    graphics.bricks_broke()
                    graphics.window.add(graphics.over,
                                        x=(graphics.window.width-graphics.over.width)/2,
                                        y=200)
                    break

                pause(FRAME_RATE)
        pause(FRAME_RATE)






if __name__ == '__main__':
    main()
