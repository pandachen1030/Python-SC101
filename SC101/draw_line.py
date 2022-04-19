"""
File: draw_line
Name:Panda
-------------------------
滑鼠點擊一次會在點擊位置製作一個圓，第二次會變成線，並且先前的圓會消失，線的起始位置圓，終點則是第二次點擊的位置。
上述為一個輪迴，要讓這個迴圈可以不斷進行。
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow()
count = 0  # 記錄點擊次數
x0 = 0  # 記錄先前製作的圓 x 座標
y0 = 0  # 記錄先前製作的圓 y 座標

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(click):
    global count, x0, y0
    hole = GOval(SIZE, SIZE, x=click.x - SIZE / 2, y=click.y - SIZE / 2)
    line = GLine(x0, y0, click.x, click.y)  # 起點為先前圓的 x,y 座標
    if count % 2 == 0:  # 若點擊次數為單制作圓；反之則做線
        x0 = click.x
        y0 = click.y
        window.add(hole)
        count += 1
    else:
        hole = window.get_object_at(x0, y0)
        window.remove(hole)
        window.add(line)
        count += 1


if __name__ == "__main__":
    main()
