"""
File: weather_master.py
Name: Panda
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
Exit = -100
Cold = 16

def main():
	"""
	TODO:找出所有輸入的數值裡的最大、最小、平均以及低於低溫特報的數值
	"""
	print('standCode "Weather Master 4.0"!')
	data = int(input('Next Temperture: (or '+str(Exit) + ' to quit) ? '))
	if data == Exit:
		print("No temperatures were entered.")
		# 一開始的值為-100則直接離開
	else:
		maximum = data
		minimum = data
		times = 0
		# 計算輸入幾次
		sum = data
		cold_days = 0
		if data < Cold:
			cold_days += 1
		while True:
			data = int(input('Next Temperture = '))
			times += 1
			if data == Exit:
				break
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
			if data < Cold:
				cold_days += 1
			sum = sum + data
			# 計算總和

		average = sum/times
		print("Highest temperature = "+str(maximum))
		print("Lowest temperature = " + str(minimum))
		print("Average = " + str(average))
		print(str(cold_days)+" cold day(s)")




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
