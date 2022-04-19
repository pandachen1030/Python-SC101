"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.gui.ginteractors import GButton
from campy.graphics.gwindow import GWindow, Region
from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gimage import GImage
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 4    # Initial vertical speed for the ball
MAX_X_SPEED = 3        # Maximum initial horizontal speed for the ball
FRAME_RATE = 1000 / 120


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        global switch
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.color = "#006400"
        self.paddle.filled = True
        self.paddle.fill_color = "#006400"
        self.window.add(self.paddle, x=(window_width-paddle_width)/2,
                        y=window_height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.color = "#008080"
        self.ball.filled = True
        self.ball.fill_color = "#008080"
        self.ball_start_x = (window_width - self.ball.width) // 2
        self.ball_start_y = (window_height - self.ball.height)//2

        self.window.add(self.ball, x=self.ball_start_x, y=self.ball_start_y)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.set_ball_velocity()
        # Initialize our mouse listeners
        self.switch = False
        onmouseclicked(self.start)
        onmousemoved(self.mouse_move)
        # Draw bricks
        self.number_of_bricks = brick_rows*brick_cols
        self.arrange_bricks()
        self.ball_delete()
        # lives
        self.lives = 0

        # Score
        self.score = 0
        self.scoreboard = GLabel("Score: " + str(self.score))
        self.scoreboard.color = "black"
        self.scoreboard.font = "Courier-20"
        self.window.add(self.scoreboard, x=20, y=self.paddle.y+45)

        self.wall = GRect(BRICK_WIDTH*2, BRICK_HEIGHT)
        self.wall.filled = True
        self.window.add(self.wall, x=(self.window.width-self.wall.width)/2,
                        y=(BRICK_SPACING+BRICK_HEIGHT)*BRICK_COLS+60)
        self.__wx = 3

        self.button = GButton('Restart')
        self.button.disable()
        self.window.add_to_region(self.button, Region.NORTH)
        self.button.add_click_handler(self.restart)
        self.restart_on = True
        self.over = GLabel("Game Over")
        self.over.color = "black"
        self.over.font = "Courier-40"

    def restart(self, event):
        self.arrange_bricks()
        self.window.remove(self.over)
        self.restart_on = True
        self.button.disable()

    def set_lives(self, new_lives):
        self.lives = new_lives

    def ball_move(self):
        self.ball.move(self.__dx, self.__dy)
        self.ball_delete()
        ball_bottom = self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2)
        ball_top = self.window.get_object_at(self.ball.x, self.ball.y)
        if self.number_of_bricks == 0:
            self.switch = False
            return self.switch
        elif self.ball.y > self.window.height:
            self.set_ball_velocity()
            self.ball.x = self.ball_start_x
            self.ball.y = self.ball_start_y
            self.delete_heart()
            self.lives -= 1
            self.switch = False
            return self.switch
        elif ball_bottom is self.wall:
            self.ball.y = self.wall.y - self.ball.height
            self.__dy *= -1
        elif ball_top is self.wall:
            self.ball.y = self.wall.y+self.wall.height
            self.__dy *= -1
        elif self.ball.x <= 0 or self.ball.x + self.ball.width > self.window.width:
            self.__dx *= -1
        elif self.ball.y <= 0:
            self.__dy *= -1
        elif self.paddle.x < self.ball.x + BALL_RADIUS < self.paddle.x + self.paddle.width \
                and ball_bottom is self.paddle:
            self.ball.y = self.paddle.y - self.ball.height
            self.__dy *= -1

    def start(self, click):
        self.switch = True
        return self.switch

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx *= -1

    def mouse_move(self, event):
        if 0 <= event.x <= self.window.width and 0 <= event.y <= self.window.height:
            if self.paddle.width/2 <= event.x <= self.window.width-self.paddle.width/2:
                self.paddle.x = event.x - self.paddle.width / 2
            elif self.paddle.x - self.paddle.width/2 < 0:
                self.paddle.x = 0
            elif self.paddle.x + self.paddle.width >= self.window.width:
                self.paddle.x = self.window.width - self.paddle.width

    def arrange_bricks(self):
        average = int(BRICK_COLS/5)
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                if 0 <= j < average:
                    brick_color = "#000000"
                elif average <= j < 2*average:
                    brick_color = "#444444"
                elif 2*average <= j < 3*average:
                    brick_color = "#666666"
                elif 3*average <= j < 4*average:
                    brick_color = "#888888"
                else:
                    brick_color = "#AAAAAA"
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                brick.color = brick_color
                brick.filled = True
                brick.fill_color = brick_color
                self.window.add(brick, x=i*(BRICK_WIDTH+BRICK_SPACING),
                                y=BRICK_OFFSET + j*(BRICK_HEIGHT+BRICK_SPACING))

    def bricks_broke(self):
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                brick = self.window.get_object_at(x=i * (BRICK_WIDTH + BRICK_SPACING),
                                y=BRICK_OFFSET + j * (BRICK_HEIGHT + BRICK_SPACING))
                if brick is not None:
                    self.window.remove(brick)

    def ball_delete(self):
        # top = self.window.get_object_at(self.ball.x-BALL_RADIUS, self.ball.y)
        # if top is not None and top is not self.paddle:
        #     self.window.remove(top)
        #     self.__dy *= -1
        for x in range(self.ball.x, self.ball.x+self.ball.width+1, self.ball.width):
            for y in range(self.ball.y, self.ball.y + self.ball.height + 1, self.ball.height):
                object = self.window.get_object_at(x, y)
                if object is not None and object is not self.paddle and object is not self.scoreboard \
                        and self.ball.y < self.paddle.y and object is not self.wall:
                    self.window.remove(object)
                    self.number_of_bricks -= 1
                    self.score += 10
                    self.scoreboard.text = "Score: " + str(self.score)
                    self.__dy *= -1
                    return self.score

    def set_heart(self):
        for i in range(self.lives):
            img = GImage("heart.png")
            self.window.add(img, x=self.window.width-27.5-17.5*i, y=self.window.height-20)

    def delete_heart(self):
        object = self.window.get_object_at(self.window.width-27.5-17.5*(self.lives-1), self.window.height-20)
        self.window.remove(object)

    def moving_wall(self):
        self.wall.move(self.__wx, 0)
        if self.wall.x+self.wall.width > self.window.width or self.wall.x<0:
            self.__wx = -self.__wx



