"""
File: boggle.py
Name: Panda
----------------------------------------
TODO: Users can enter 4*4 letters and the function will start from the first letter to find
whether it can form a word with the surrounding. If words with more than four letters will be printed.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# global variable
d = {}
row_dict = {}
current_lst = []


def main():
	"""
	TODO: Let users input 4*4 letters, and check whether it matches the format. start boggle game
	"""
	read_dictionary()
	for i in range(4):
		row = input(f"{i+1} row of letters: ")
		row.lower()
		if len(row) != 7 or check(row):
			print("Illegal input")
			break
		else:
			row_dict[i] = row.replace(" ", "")
	start = time.time()
	if len(row_dict) == 4:  # to make sure there is 4*4 letters
		for j in range(4):
			for k in range(4):
				last_position = (j, k)  # record last position to avoid going back
				find_word(row_dict[j][k], j, k, last_position)
		print(f"There are {len(current_lst)} words in total.")
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(current_word, current_p1, current_p2, last_position):
	for x in range(-1, 2, 1):
		for y in range(-1, 2, 1):
			next_p1 = current_p1 + x
			next_p2 = current_p2 + y
			if x == 0 and y == 0:   # to avoid link itself
				pass
			elif (next_p1, next_p2) == last_position:  # to avoid going back
				pass
			elif 0 <= next_p1 < 4:
				if 0 <= next_p2 < 4:
					# choose
					current_word += row_dict[next_p1][next_p2]
					# explore
					if has_prefix(current_word):
						# print current string if it is more than 4 letters and in dict
						if len(current_word) >= 4 and current_word not in current_lst:  # avoid printing same words
							if current_word in d[current_word[:len(current_word) + 1]]:
								current_lst.append(current_word)
								print(f'Found "{current_word}"')
						find_word(current_word, next_p1, next_p2, (current_p1, current_p2))
					# un-choose
					current_word = current_word[:-1]


def check(row):
	"""
	:param row: users input 4 letters
	:return: boolean
	"""
	for i in range(len(row)-1):
		# check if there is letters with spaces
		if row[i].isalpha() and row[i+1].isalpha():
			return True
		# check if there is no digit
		if row[i].isdigit() or row[i+1].isdigit():
			return True
	# check if there is 4 letters
	row.replace(" ", "")
	if len(row) < 4:
		return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, "r") as f:
		for line in f:
			word = line.strip()
			for i in range(len(word)):
				if word[:i + 1] in d:
					d[word[:i + 1]].append(word)
				else:
					d[word[:i + 1]] = [word]


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	if sub_s[:len(sub_s) + 1] in d:  # check if the string in dict
		return True
	return False


if __name__ == '__main__':
	main()
