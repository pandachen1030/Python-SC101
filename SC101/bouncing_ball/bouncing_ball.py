"""
File: bouncing_ball
Name:Panda
-------------------------
在指定位置生出球，點擊滑鼠後球遵守重力加速度原則向下墜落且向右移動，當觸底時反彈、動能持續衰減。
當球跑出畫面後會回到初始位置，等待重新開始，過程中滑鼠點擊不會影響。
三次後無法再次進行。
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
switch = True
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(bounce)


def close(click):
    pass


def bounce(click):
    global count, switch
    onmouseclicked(close)  # 取代onmouseclicked(bounce) 讓他不執行 bounce()
    ball_y = 1  # 球向下墜的速度，假設初始值為 1
    while True and count <= LIFE: # 當執行次數超過指定數量時會終止
        ball.move(VX, ball_y)  # 球向右下墜的速度，並且有一個重力加速度
        ball_y += GRAVITY
        if ball.y + ball.height >= window.height:
            ball_y = -ball_y * REDUCE
        if ball.x - ball.width >= window.width:
            break
        pause(DELAY)
    window.add(ball, START_X, START_Y)
    count += 1
    onmouseclicked(bounce)  # 再次執行 onmouseclicked(bounce)

if __name__ == "__main__":
    main()
