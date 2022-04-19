"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
# global variable
d = {}
current_lst = []
count = 0


def main():
    """
    TODO:將使用者輸入的單字重組，尋找字典裡面有的單字，並且 print 出來
    """
    global count, current_lst
    print(f"Welcome to stanCode ''Anagram Generator'' (or -1 to quit)")
    read_dictionary()
    while True:
        s = input("Find anagrams for: ")
        start = time.time()
        if s == EXIT:
            break
        else:
            print("Searching...")
            find_anagrams(s)
            print(f"{count} anagrams: {current_lst}")
            count = 0  # 每次結束後要歸零計數器
            current_lst = []  # 每次結束後要清空列表
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    with open(FILE, "r") as f:
        for line in f:
            word = line.strip()
            for i in range(len(word)):  # 將每個字從頭到尾都做成 dic 方便後續尋找
                if word[:i+1] in d:
                    d[word[:i+1]].append(word)
                else:
                    d[word[:i+1]] = [word]


def find_anagrams(s):
    """
    :param s:輸入的單字
    :return:用 recursive 去重組以及 print
    """
    find_anagrams_helper(s, "")


def find_anagrams_helper(s, current_s):
    global count, current_lst
    if len(current_s) == len(s) and current_s not in current_lst:
        if current_s in d[current_s[:len(current_s)+1]]:
            print(f"Found: {current_s}")
            print("Searching...")
            current_lst.append(current_s)
            count += 1
    else:
        for i in range(len(s)):
            if s[i] in current_s and current_s.count(s[i]) == s.count(s[i]):
                pass
            else:
                # choose
                current_s += s[i]
                if has_prefix(current_s):
                    # explore
                    find_anagrams_helper(s, current_s)
                # un-choose
                current_s = current_s[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: 當前要檢查的字串
    :return: 是否有在 dict 裏面，return True or False
    """
    if sub_s[:len(sub_s)+1] in d:  # 看目前字串是否有在 dict 裏面
        return True
    return False


if __name__ == '__main__':
    main()
