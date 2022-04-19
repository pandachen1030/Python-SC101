"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
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
MAX_X_SPEED = 7        # Maximum initial horizontal speed for the ball
FRAME_RATE = 1000 / 120
COLORS = ['red', 'orange', 'yellow', 'green', 'blue']


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.color = "pink"
        self.paddle.filled = True
        self.paddle.fill_color = "pink"
        self.window.add(self.paddle, x=(window_width-paddle_width)/2,
                        y=window_height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.color = "blue"
        self.ball.filled = True
        self.ball.fill_color = "blue"
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

    def set_lives(self, new_lives):
        self.lives = new_lives

    def ball_move(self):
        self.ball.move(self.__dx, self.__dy)
        # self.ball_delete()
        if self.number_of_bricks == 0:
            # when bricks are all broke, the game is over
            self.switch = False
        elif self.ball.y > self.window.height:
            self.set_ball_velocity()
            self.ball.x = self.ball_start_x
            self.ball.y = self.ball_start_y
            self.lives -= 1
            self.switch = False
        elif self.ball.x <= 0 or self.ball.x + self.ball.width > self.window.width:
            self.__dx *= -1
        elif self.ball.y <= 0:
            self.__dy *= -1

    def start(self, click):
        self.switch = True  # when user clicks the mouse, the switch will turn open
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
        average = int(BRICK_COLS/len(COLORS))
        color_ct = -1
        for i in range(BRICK_ROWS):
            if i % average == 0:
                color_ct += 1
            for j in range(BRICK_COLS):

                # if 0 <= j < average:
                #     brick_color = "red"
                # elif average <= j < 2*average:
                #     brick_color = "orange"
                # elif 2*average <= j < 3*average:
                #     brick_color = "yellow"
                # elif 3*average <= j < 4*average:
                #     brick_color = "green"
                # else:
                #     brick_color = "blue"
                brick_color = COLORS[color_ct % len(COLORS)]
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                brick.color = brick_color
                brick.filled = True
                brick.fill_color = brick_color
                self.window.add(brick, x=j*(BRICK_WIDTH+BRICK_SPACING),
                                y=BRICK_OFFSET + i*(BRICK_HEIGHT+BRICK_SPACING))

    def ball_delete(self):
        for x in range(self.ball.x, self.ball.x+self.ball.width+1, self.ball.width):
            for y in range(self.ball.y, self.ball.y + self.ball.height + 1, self.ball.height):
                object_ = self.window.get_object_at(x, y)
                if object_ is self.paddle:
                    # to make sure that the ball is in the area of paddle and hits it
                    self.ball.y = self.paddle.y - self.ball.height
                    self.__dy *= -1
                    return
                elif object_ is not None and object_ is not self.paddle and object_ is not self.scoreboard:
                    self.window.remove(object_)
                    self.number_of_bricks -= 1
                    self.score += 10
                    self.scoreboard.text = "Score: " + str(self.score)
                    self.__dy *= -1
                    return self.score