"""
File: caesar.py
Name: Panda
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO:使用者輸入位移的次數，並且輸入密碼，讓程式去解碼
    """
    n = int(input("Secret umber: "))
    string = input("What's the ciphered string? ")
    string = string.upper()
    ans = decipher(n, string)
    print("The deciphered string is: " + ans)


def decipher(n, string):
    ans = ""
    for i in range(len(string)):
        a = string[i]
        b = ALPHABET.find(a)
        if b == -1:
            ans = ans + string[i]
            # 非英文字母的內容可以直接呈現，不需解碼
        elif b+n >= 26:
            # 避免使用者輸入過長的位移數字
            ans = ans + ALPHABET[(b+n)%26]
        else:
            ans = ans + ALPHABET[b+n]
    return ans

#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
