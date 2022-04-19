"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""
	find the largest digit in the number
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: a number which is inputted
	:return: recursion for helping us to find largest digit
	"""
	if n < 0:
		n *= -1
	largest_n = 0
	return find_largest_digit_helper(n, largest_n)


def find_largest_digit_helper(n, largest_n):
	"""
	:param n: a number which is inputted
	:param largest_n: currently largest number
	:return: recursion for helping us to find largest digit
	"""
	if n == 0:
		return largest_n
	else:
		number = n % 10
		if number > largest_n:
			largest_n = number
		return find_largest_digit_helper(n//10, largest_n)


if __name__ == '__main__':
	main()
