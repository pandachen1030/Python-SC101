"""
File: hailstone.py
Name: Panda
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    當某數為奇數時成3加1；反之除2，並且得出的數值依舊重複上述動作直到得出1為止
    並且必須紀錄每個計算步驟
    """
    print("This program computes Hailstone sequences.")
    print("")
    n = int(input("Enter a number: "))
    c = 0
    # 用 c 來計算步數
    if n == 1:
        pass
    else:
        while True:
            if n % 2 ==1:
                a = n
                c+=1
                n = n * 3 + 1
                print(str(a)+' is odd, so I make 3n+1: '+str(n))
                if n < 2:
                    break
            else:
                b = n
                c += 1
                n = n // 2
                print(str(b) + ' is even, so I take half: '+str(n))
                if n < 2:
                    break
    print('It took '+str(c)+' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
