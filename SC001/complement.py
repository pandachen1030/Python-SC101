"""
File: complement.py
Name: Panda
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    TODO:輸入基因序列後可以找到對應的互補檢基
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    dna = dna.upper()
    complement = build_complemen(dna)
    print("The complement of " + dna + " is " + complement)


def build_complemen(dna):
    ans = ""
    for base in dna:
        if base == "A":
            ans += "T"
        elif base == "T":
            ans += "A"
        elif base == "C":
            ans += "G"
        elif base == "G":
            ans += "C"
    return ans

###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
