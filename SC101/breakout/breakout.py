"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gimage import GImage

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    graphics.set_lives(lives)  # setup the lifes to be NUM_LIVES

    # Add the animation loop here!
    while True:
        if graphics.switch and graphics.lives > 0:
            # ensure the switch is open and the life is bigger than 3, so the game can be started
            graphics.ball_move()
            graphics.ball_delete()
            pause(FRAME_RATE)



        pause(FRAME_RATE)





if __name__ == '__main__':
    main()
