# i = 0
# num1 = 0
# num2 = 0
#
# num1 = int(input("enter first number:"))
# if num1%2!=0:
#     num1+=1
# else:
#     num1+=2
# num2 = int(input("enter second number:"))
#
# for i in range(num1,num2,2):
#     print(i)
# if num2 > num1:
#     if num2 % 2 != 0:
#         num2 += 1
#     else:
#         num2 += 2
#     for i in range(num2,num1,2):
#         print(i)
#
#
# print("end of session")



#4.2
# i = 2
# a = 1
# num = int(input("enter number:"))
# for a in range(i,num):
#     if num%a==0:
#         print("you are good")
#         break
# else:
#     print("number rishoni")


# 4.3
# from random import randint
# system_guess = randint(1,9)
# num = int(input("enter number:"))
# while num!=system_guess:
#     if num>system_guess:
#         print("enter lower number:")
#         num = int(input("enter number:"))
#     else:
#         print("enter higher number:")
#         num = int(input("enter number:"))
# print("you are right!!!")


# #4.4
# from random import randint
# min = 0
# max = 100
# high = 0
# low = 0
# system_guess = randint(min,max)
# print(system_guess)
# guessing = True
#
# while guessing:
#     user = (input("high,low or your number?:"))
#     if user == "high":
#         min = system_guess
#         high = randint(min,max)
#         print(high)
#         system_guess = high
#     if user == "low":
#         max = system_guess
#         low =randint(min,max)
#         print(low)
#         system_guess = low
#
#     print(f'minimum is {min}')
#     print(f'maximum is {max}')
#
#
#     if user == "number":
#         guessing = False
# print("easy money!")


#4.5
# counter = 0
# password = int(input("please enter password:"))
# sec = int(input("please enter password identification:"))
#
# while sec != password:
#     print(f"wrong identification, try number{counter+1}")
#     if sec == password:
#         print("login suecced")
# sec = True
#
#
#         counter += 1
#         print("wrong!")
#         sec = int(input(f"try number {counter} please try again:"))
#
#         if counter== 5:
#             print("too many tries youre locked!")
#             break
# word = (input("enter word:"))
# i = 0
# for letter in word:
#     i+=1
#     for a in range(0,i):
#         print(letter,end="")
# i=0
# num = int(input("insert number:"))
# sum = 0
# for i in num:
#     sum+=i
# print(sum)















