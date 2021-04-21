from time import *
from datetime import *

##### num = sleep(5)    #נותנת השהייה של 5 שניות לפני הדפסת התשובה
# print(num)

#####print(localtime()) #מחזירה זמן מקומי

#####print(gmtime()) ## נותן את השעה הנוכחית בקו גריניץ'

#####print(asctime()) ##מחזיר את הזמן במחרוזת

#####print(ctime())  ##מעביר משניות לזמן ותאריך במחרוזת

#####print(datetime.now()) ## מחזירה את התאריך המוכחי

#####print(datetime(2002, 4, 29, 23, 59, 59) - datetime.now())

#####print(datetime.now() + timedelta(days) ##מחשב את התאריך בעוד מספר הימים שהוזנו

# print(datetime.now())
# now = datetime.now()
# year = now.strftime("%Y")
# print("year:",year)
# year = now.strftime("%Y")
# month = now.strftime("%m")
# day = now.strftime("%d")
# print(f"date:{day}/{month}/{year}")
# clock = now.strftime("%H:%M:%S")
# print(f"clock: {clock}")

#9.1
# name = input("enter your name: ")
# age = int(input("enter your age: "))
# now = datetime.now()
# year = now.strftime("%Y")
# year = int(year) + 100 - age
# print(f"{name} will be 100 years old in the year :{year}")

#9.2
# america = strftime("%m/%d/%y")
# europa = strftime("%d/%m/%y")
# print(f"the american date is: {america}")
# print(f"the european date is: {europa}")

#9.3
# day = int(input("day: "))
# month = int(input("month: "))
# year = int(input("year: "))
# date1 = datetime(year, month, day,)
# print(date1)

#9.4

# num = int(input("enter day 1-7: "))
# today = datetime.now()
# day = int(input("day:"))
# month = int(input("monthh:"))
# year = int(input("year:"))("



