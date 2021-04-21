#1
# from random import randint
# list1=[]
# for i in range(10):
#     list1.append(randint(1,100))
# print(list1)
#list1=[1,2,3,4,5,6,7,8,9,10]
#3
# print(list1[9:6:-1])

#4
# print(list1[::-1])

#5
#print(list1[::2])

#6
#print(list1[:5])

#7
#print(list1[::2])

#8
# list2 = list1.copy()
# num = int(input("number: "))
# list2[7:9]=[num]
# list2.append(num)
# print(list2)

#9
# list2 = list1.copy()
# num = int(input("number: "))
# list2[-3:]=[num]
# print(list2)

#10
# list2=list1.copy()
# for i in list2:
#     if i%3==0:
#         list2.append(i)
#         list2.remove(i)
# print(list2)

#11
# list1 = [1,1]
# for i in range(2,20):
#     i = list1[i-1]*2
#     list1.append(i)
# print(list1)

#12
# str = input("word")
# list = ""
# count = 0
# for i in str:
#     count+=1

#13
# from random import randint
# list = []
# choice = int(input("enter number:"))
# for i in range(20):
#     num = randint(1,100)
#     list.append(num)
#     if num == choice:
#         list.remove(num)
# print(list)

#14
# num = int(input("enter number: "))
# list = []
# for i in range(1,num):
#     if num%i==0:
#         list.append(i)
# print(list)

#15
# list = [1,1]
# num = int(input("enter number: "))
# for i in range(2,num):
#     i= list[(i-1)]*2
#     list.append(i)
# print(list)

#16
# list1=[1,3,4,5,2,3,4,5,3,2]
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

#17
# list1=[1.5,3,4,5,3,4,5,3,4.5]
# list2=[0,-1,2,"a","b","c"]
# for i in list1:
#     if i in list2:
#         print("same number")
#         break
# else:
#     print("no same number")
#18

# list1=["12","gf","rew","789","458798584","aghufivbhugra","wbhi37849w"]
# count=0
# for s in list1:
#     if len(s)>3 and s[0]==s[-1]:
#         count+=1
# print(count)

#19
# from random import randint
# list1 = []
# for i in range(10):
#     num = randint(1,5)
#     list1.append(num)
# list2 = []
# print(list1)
# for i in list1:
#     count = 0
#     kayam=False
#     for g in list2:
#         if i == int(g[0]):
#             kayam=True
#             break
#     if kayam==True:
#         continue
#     for a in list1:
#         if i == a:
#             count+=1
#
#     list2.append(str(i)+"-"+str(count))
#
# print(list2)

#20
# from random import randint
# list1=[]
#
# for i in range(10):
#     list1.append(randint(1,10))
# num = int(input("enter number: "))
# for a in list1:
#     if num== a:
#         print(list1)
#         print(num,"-",list1.index(num))
#         break
# if num not in list1:
#     print("youre number is not in the list")


#21
# from random import randint
# str1=""
# guess = ""
# for i in range(4):
#     num = randint(0,9)
#     str1+=str(num)
#
# correct = False
# while correct==False:
#     hits = 0
#     bools = 0
#     guess = input("enter number: ")
#     for i in range(4):
#         if guess[i]==str1[i]:
#             hits+=1
#     bools = 4 - hits
#     if hits == 4:
#         print("you win!")
#         break
#     print(f"hits: {hits}  |  bools: {bools}")

#22























