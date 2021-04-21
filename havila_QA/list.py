#5.1
# list1 = []
# sum = 0
# for i in range(7):
#     num = int(input("enter number: "))
#     sum+=num
#     list1.append(num)
# print(f"the max number is:{max(list1)}")
# print(f"the min number is: {min(list1)}")
# print(sum/7)

#5.3
# from random import randint
# list1 =[]
# for i in range(10):
#     list1.append(randint(1,1000))
# print(list1)

#5.4
# list1 = []
# list2 = []
# list3 = []
# for i in range(5):
#     num = int(input("enter number for list1: "))
#     list1.append(num)
# for i in range(5):
#     num = int(input("enter number for list2: "))
#     list2.append(num)
# list3 = list1 + list2
# print(list3)
# print(f"the list lengh is: {len(list3)}")

#5.5
# list1=[]
# count1 = 0
# list2=[]
# count2 = 0
# list3=[]
# for i in range(10):
#     grade = int(input("enter grade: "))
#     if grade > 60:
#         list1.append(grade)
#         count1+=1
#     if grade < 60:
#         list2.append(grade)
#         count2 +=1
# print(f"there are {count1} student who passed with the grades:{list1}")
# print(f"there are {count2} students who failed with the grade: {list2}")

#5.6
# list1  = [1,2,3,4,5,6,7,8,9,10]
# list2 = list1.copy()
# print (list1[7:])
# print(list1[::-1])
# print(list1[2::2])
# print(list1[::2])
# list2[4]=int(input('number:'))
# list2[5]=int(input('number:'))
# num=int(input('number:'))
# list2.append(num)
#
# print(list2)
# list3=[]
# for i in list1:
#     i*=2
#     list3.append(i)
# print(list3)
# list4 = list1[0],list1[9]
# print(list4)
