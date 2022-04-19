"""
File: hangman.py
Name: Panda
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO: 要猜出隨機的英文單字是什麼，並且可以設定答題次數
    """
    ans = random_word()
    b = ""
    c = N_TURNS
    # 常數不會變更，所以用變數去裝它，以便紀錄剩餘答題數
    for i in range(len(ans)):
        b += '-'
        # 看有多少字，讓字母皆被「-」取代
    print("The word looks like: " + b)
    print("You have " + str(N_TURNS) + " guesses left.")
    d = b
    # 再找一個變數去記錄目前已被猜到的文字
    while True:
        b = d
        if d == ans:
            print("You wi!!")
            print("The word was: " + ans)
            break
        guess = input("Your guess: ")
        alpha = str.isalpha(guess)
        # 確保都是字母
        guess = guess.upper()
        e = ans.find(str(guess))
        # 去看輸入的字母有沒有在單字裡
        if alpha == False:
            print("illegal format.")
        elif len(guess) > 1:
            print("illegal format.")
            # 避免輸入兩個以上字母
        elif e == -1:
            print("There is no " + guess + "'s in the word.")
            print("The word looks like: " + b)
            c -= 1
            if c == 0:
                print("You are completely hung:(")
                print("The word was: " + ans)
                break
            else:
                print("You have " + str(c) + " guesses left.")
        else:
            d = ""
            for j in range(len(ans)):
                if guess == ans[j]:
                    d += ans[j]
                else:
                    d += b[j]
            print("You are correct!")
            print("The word looks like: " + d)
            print("You have " + str(c) + " guesses left.")



def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
