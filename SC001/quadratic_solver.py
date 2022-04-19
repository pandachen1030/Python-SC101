"""
File: quadratic_solver.py
Name: Panda
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	方程式計算，一開始要求使用者輸入三個數值，找出根號
	"""
	print("stanCode Quadratic Solver!")
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	d = b*b-4*a*c
	if d<0:
		print("No real roots")
		# 根號內數字為負數則無解
	else:
		e = math.sqrt(d)
		x1 = (-1 * b + e) / 2 * a
		x2 = (-1 * b - e) / 2 * a
		if d==0:
			print('One root: '+str(x1))
		else:
			print('Two roots: '+str(x1)+","+str(x2))





###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
