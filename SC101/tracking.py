"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause




def main():
	"""
	TODO:
	"""
	num = b(5, 2)
	print(num)


def b(n, k):
	if k == 0 or k == n:
		print("Base Case!")
		return 2
	else:
		return b(n-1, k-1) + b(n-1, k)


if __name__ == '__main__':
	main()