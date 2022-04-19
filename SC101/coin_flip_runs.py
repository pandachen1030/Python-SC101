"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO:每次程式會隨機生成Ｔ或Ｈ，每次遇到連續的字算一個回合，使用者可以輸入任意整數，去決定要有幾次重複的回合才停止
	"""
	th = "TH"
	print("Let's flip a coin!")
	run1 = int(input("Number of runs: "))
	str1 = ""
	# 建立一個空字串來記錄
	n = r.randrange(0, 2)
	# n為0-1的隨機數字
	roll = th[n]
	# roll為隨機Ｔ或Ｈ
	str1 += roll
	# 把roll加入字串str1
	while True:
		count_runs = 0
		# 用來計算目前字串有幾個回合
		n = r.randrange(0, 2)
		roll = th[n]
		str1 += roll
		is_in_a_row = True
		# 製作一個開關，可進行切換
		for i in range(len(str1)):
			# 做一個for loop 看現在這個字串有幾個回合
			if i+1 < len(str1):
				if str1[i] == str1[i+1]:
					if is_in_a_row:
						count_runs += 1
						is_in_a_row = False
						# 當有連續三次以上同樣的文字開關會呈現關閉，避免重複計算
				else:
					is_in_a_row = True
					# 用出現不同的文字以後調整開關為開啟
		if count_runs == run1:
			break
	print(str1)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
