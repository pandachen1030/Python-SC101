"""
File: class_reviews.py
Name:
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = -1


def main():
    """
    TODO:紀錄001以及101的分數，並計算最高分、最低分以及平均
    輸入
    """
    count_001 = 0
    count_101 = 0
    # 計算兩堂課程分別輸入了幾次成績
    sum_001 = 0
    sum_101 = 0
    # 算分別的總和成績
    class_number = input("Which class? ")
    class_number = class_number.upper()
    if class_number == str(EXIT):
        print("No class scores were entered.")
    # 一開始就輸入離開的狀態
    else:
        if class_number == "SC001":
            score_001 = int(input("Score: "))
            max_001 = score_001
            min_001 = score_001
            max_101 = "no"
            min_101 = "no"
            # 用一個代號指定為另一個課程目前的狀態
            count_001 += 1
            sum_001 += score_001
        elif class_number == "SC101":
            score_101 = int(input("Score: "))
            max_101 = score_101
            min_101 = score_101
            max_001 = "no"
            min_001 = "no"
            count_101 += 1
            sum_101 += score_101
        while True:
            class_number = input("Which class? ")
            class_number = class_number.upper()
            if class_number == str(EXIT):
                break
            # 輸入離開的常數後結束程式
            elif class_number == "SC001":
                score_001 = int(input("Score: "))
                count_001 += 1
                sum_001 += score_001
                if max_001 == "no":
                    max_001 = score_001
                    # 若目前最大值為先前指定的代號，則表示目前沒有數值輸入，所以將目前輸入的數字做替換
                elif score_001 > max_001:
                    max_001 = score_001
                    # 若目前輸入的值大於最大值，則數字做替換
                if min_001 == "no":
                    min_001 = score_001
                    # 若目前最小值為先前指定的代號，則表示目前沒有數值輸入，所以將目前輸入的數字做替換
                elif score_001 < min_001:
                    min_001 = score_001
                    # 若目前輸入的值小於最小值，則數字做替換
            elif class_number == "SC101":
                score_101 = int(input("Score: "))
                count_101 += 1
                sum_101 += score_101
                if max_101 == "no":
                    max_001 = score_001
                elif score_101 > max_101:
                    max_101 = score_101
                if min_101 == "no":
                    min_101 = score_101
                elif score_101 < min_101:
                    min_101 = score_101

        print("=============SC001=============")
        if count_001 != 0:
            avg_001 = sum_001 / count_001
            # 計算平均
            print("Max(001): " + str(max_001))
            print("Min(001): " + str(min_001))
            print("Avg(001): " + str(avg_001))
        else:
            print("No score for SC001")
        print("=============SC101=============")
        if count_101 != 0:
            avg_101 = sum_101 / count_101
            print("Max(101): " + str(max_101))
            print("Min(101): " + str(min_101))
            print("Avg(101): " + str(avg_101))
        else:
            print("No score for SC101")



# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
