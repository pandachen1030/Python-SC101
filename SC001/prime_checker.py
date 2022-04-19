"""
File: prime_checker.py
Name: Panda
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

Exit = -100

def main():
	"""
	確認質數，在某數減一到2之間皆沒有任何一數可以整除某數則為質數
	"""
	print('Welcome to the prime checker!')
	while True:
		n = int(input('Enter n: '))
		a = n - 1
		if n == Exit:
			print('Have a good one!')
			break
			# n 為指定數字則離開迴圈，結束找質數的作業
		if n == 2:
			print(str(n) + ' is prime number.')
		while n % a != 0:
			a -= 1
			if a < 2:
				print(str(n) + ' is prime number.')
			elif n % a == 0:
				print(str(n) + ' is not prime number.')













###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
