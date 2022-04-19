"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_position = width//len(YEARS)*year_index
    return x_position

def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE),
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE),
                       width=LINE_WIDTH)
    for i in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i), 0,
                           GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT,
                           width=LINE_WIDTH)
        canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX,
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)

def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    name_y = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 1000
    for i in range(len(lookup_names)):
        color = i % len(COLORS)  # 取餘數去看目前的資料要用哪個顏色
        name = lookup_names[i]
        if name in name_data:
            for j in range((len(YEARS)-1)):
                year = YEARS[j]
                next_year = YEARS[j+1]
                if str(year) in name_data[name]:
                    rank = int(name_data[name][str(year)])
                else:
                    rank = MAX_RANK+1
                if str(next_year) in name_data[name]:
                    next_rank = int(name_data[name][str(next_year)])
                else:
                    next_rank = MAX_RANK+1

                if rank > MAX_RANK and next_rank > MAX_RANK:  # 若起點年份與下一年的排名都沒紀錄
                    canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, j),
                                       GRAPH_MARGIN_SIZE + name_y * MAX_RANK,
                                       GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, j + 1),
                                       GRAPH_MARGIN_SIZE + name_y * MAX_RANK,
                                       width=LINE_WIDTH, fill=COLORS[color])
                    canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, j) + 5,
                                       GRAPH_MARGIN_SIZE + name_y * rank,
                                       text=f"{name} *", anchor=tkinter.SW, font="times 10",fill=COLORS[color])
                elif rank > MAX_RANK:  # 若僅有起點年份的排名沒紀錄
                    canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, j),
                                       GRAPH_MARGIN_SIZE + name_y * MAX_RANK,
                                       GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, j + 1),
                                       GRAPH_MARGIN_SIZE + name_y * next_rank,
                                       width=LINE_WIDTH, fill=COLORS[color])
                    canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, j) + 5,
                                       GRAPH_MARGIN_SIZE + name_y * rank,
                                       text=f"{name} *", anchor=tkinter.SW, font="times 10",fill=COLORS[color])
                elif next_rank > MAX_RANK:  # 若僅有下一年的排名沒紀錄
                    canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, j),
                                       GRAPH_MARGIN_SIZE + name_y * rank,
                                       GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, j + 1),
                                       GRAPH_MARGIN_SIZE + name_y * MAX_RANK,
                                       width=LINE_WIDTH, fill=COLORS[color])
                    canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, j) + 5,
                                       GRAPH_MARGIN_SIZE + name_y * rank,
                                       text=f"{name} {rank}", anchor=tkinter.SW, font="times 10",fill=COLORS[color])
                else:
                    canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, j),
                                       GRAPH_MARGIN_SIZE + name_y * rank,
                                       GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, j + 1),
                                       GRAPH_MARGIN_SIZE + name_y * next_rank,
                                       width=LINE_WIDTH,fill=COLORS[color])
                    canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, j) + 5,
                                       GRAPH_MARGIN_SIZE + name_y * rank,
                                       text=f"{name} {rank}", anchor=tkinter.SW, font="times 10",fill=COLORS[color])
        # 最後一個年份需要再補一次姓名標籤
        if next_rank > MAX_RANK:
            canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, j + 1) + 5,
                               GRAPH_MARGIN_SIZE + name_y * next_rank,
                               text=f"{name} *", anchor=tkinter.SW, font="times 10",fill=COLORS[color])
        else:
            canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, j + 1) + 5,
                               GRAPH_MARGIN_SIZE + name_y * next_rank,
                               text=f"{name} {next_rank}", anchor=tkinter.SW, font="times 10",fill=COLORS[color])



# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
