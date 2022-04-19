"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        items = soup.find_all('table', {'class': "t-stripe"})
        male_total = 0
        female_total = 0
        for item in items:
            content = item.tbody.text.split()  # 把 content 的 str 轉成 list
            for i in range(len(content[:1000])):  # 前一千筆資料包含排名、男女姓名及數量，五筆資料一個循環
                if i % 5 == 2:  # 此為男生數量
                    number = ""
                    for j in range(len(content[i])):  # 確保新字串內都是數字
                        if content[i][j].isdigit():
                            number += content[i][j]
                    male_total += int(number)
                elif i % 5 == 4:  # 此為女生數量
                    number = ""
                    for j in range(len(content[i])):
                        if content[i][j].isdigit():
                            number += content[i][j]
                    female_total += int(number)

        print("Male Number: " + str(male_total))
        print("Female Number: " + str(female_total))






if __name__ == '__main__':
    main()
