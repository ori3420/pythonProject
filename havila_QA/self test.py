###-------basics-------###
#1.
# num1=int(input("insert number:"))
# num2=int(input("insert number:"))
# print(f"{str(num1)}+{str(num2)}={num1+num2}")
# print(f"{str(num1)}-{str(num2)}={num1-num2}")
# print(f"{str(num1)}*{str(num2)}={num1*num2}")
# print(f"{str(num1)}/{str(num2)}={num1/num2}")

#5
# num1 = int(input("enter number1:"))
# num2 = int(input("enter number2:"))
# num3 = int(input("enter number3:"))
# num1 = num1*100
# num2 = num2*10
# num3 = num3
# num4 = num1 + num2 + num3
# print(num4, num4*2)

#6
# num1 = int(input("enter number1:"))
# num2 = int(input("enter number2:"))
# print((num1/num2),(num1//num2),(num1%num2))

###-------basic loops-------###
#1
# num = 0
# sum = 0
# counter = 0
# for i in range(6):
#     num = int(input("please enter number:"))
#     sum+=num
#     counter+=1
# print(sum,sum/counter)

#4
# num = 0
# sum = 0
# i = 0
# for i in range(10,100):
#     if i%10==0:
#         sum+=i
# print(sum)

#7
# right = 0
# sum = 0
# for i in range(5):
#     num = int(input("please enter number:"))
#     right = num%10
#     sum+=right
#
# print(sum)

#8
# num = int(input("enter number:"))
# for i in range(1,num+1):
#     if i%5==0:
#         print(i)

#9
# counter = 0
# num = int(input("number:"))
# for i in range(2,num+1):
#     if i%2==0:
#         print(i)

#10
# counter = 0
# num = int(input("number:"))
# while num!=0:
#     num = int(input("number:"))
#     if num%3==0 or num%7==0:
#         counter+=1
# print(f"there are {counter} numbers divided by 3 and 7")


###-------while excersise-------###

#1
# num = int(input("number:"))
# sum=0
# while num>=100 and num<=999:
#
#     sum= (num%10)+(num//100)+(num//10%10)
#     print(sum)
#     num = int(input("number:"))
# print("invalid number, end of session")

#3
# num1 = int(input("number:"))
# num2 = int(input("number2:"))
# while num1%2==0 and num2%2==0:
#     print(num1+num2)
#     num1 = int(input("number:"))
#     num2 = int(input("number2:"))
# print(num1*num2)

#4
# num1 = int(input("number1:"))
# num2 = int(input("number2:"))
# while num1+num2==10:
#     print("good job!")
#     num1 = int(input("number1:"))
#     num2 = int(input("number2:"))
# print("numbers total not equal 10")


####-------java-(2)תרגילי לולאות-------##

#1
#maxgrade =0
#sum = 0
#count = 0
#grade = 0
#while 0<=grade and grade<=100:
#    grade = int(input("grade:"))
#    if grade>100 or grade<0:
#        break
#
#    sum+=grade
#    count+=1
#
#    if grade > maxgrade:
#        maxgrade = grade
#
#
#
#print("invalid grade")
#print(f"the highest grade is: {maxgrade}")
#print(f"the avg is:{sum/count}")
#print(f"the diff between highest grade and avg is: {maxgrade-sum/count}")





#2
# password = input("insert password:")
# for i in range(1,6):
#     con = input("insert password again:")
#     if password == con:
#         print("login succes")
#         break
#     if i == 5:
#         print("out of tries!")
#         break
#     if password!= con:
#         print(f"try number #{i} failed, try again")



#3
# while True:
#
#     num = input("number:")
#     counter = 0
#     for i in num:
#         counter+=1
#
#     print(counter)





####--------תרגילי לולאות##4

#1---!!!!
# i = 0
# num = int(input("number:"))
# for i in range(2,num):
#     if num %i == 0:
#         print("num is not prime")
#         break
# else:
#     print("number is prime")

#2
# while True:
#     num = input("number:")
#     counter = 0
#     for digit in num:
#         counter +=1
#     print(counter)
#

#3

# num = int(input("number:"))
# min = num
# while num!=0:
#     num = int(input("number:"))
#     if num ==0:
#         break
#     if num<0:
#         continue
#     if num<min:
#         min = num
#
# print(min)



#4
# num = int(input("number:"))
# while num//10 != 0 :
#     num = num//10
# print(num)

#5
# num2 = int(input("number:"))
# num = num2
# counter = 1
# for i in range(6):
#     num2 = int(input("number:"))
#     if num2 > num:
#         num = num2
#         counter+=1
#
#     if num < num2:
#         continue
# print(counter)

#6
#num = int(input("number: "))
#invert_num = 0
#while num//10 !=0:
#    invert_num = invert_num * 10 + num%10 #להוסיף למחברת!
#    num//=10
#invert_num = invert_num * 10 + num
#print(invert_num)
#print(invert_num*2)

#7
# for i in range(2):
#     num1 = int(input("enter num1: "))
#     num2 = int(input("enter num2: "))
#     if num2>num1:
#         print("first number must be bigger than second")
#         continue
#     if num2<num1:
#         print(num1//num2)


#8
# num = 0
# min = 0
# min = int(input("number: "))
# for number in range(4):
#     num = int(input("number: "))
#     for number in range(2,10):
#         if num%number==0:
#             if num > min:
#                 num = min
#             else:
#                 continue
#         else:
#             continue
# if num%number==0:
#     print(num)
# else:
#     print("no number!")

#####--------loops 4.5-------#####
# i = 0
# num = int(input("number: "))
# for i in range(0,num+1,i+):


#4.6
counter = 0
list = input("enter list:")
num = input("enter digit:")
for digit in (list):
    if digit == num:
        counter+=1
    else:
        continue
print(counter)




























