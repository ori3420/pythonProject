#1
# num = int(input("enter number:"))
# while num > 99 and num < 1000:
#     print((num//100) + (num//10%10) + (num%10))
#     num = int(input("enter number:"))
# print("error, end of session")


# 2
# age = input("please enter age:")
# age = int(age)
# while 0<=age<=120:
#     if 0<=age<=18:
#         print("child")
#     if 19<=age<=60:
#         print("adult")
#     if 61<=age<=120:
#         print("senior")
#     age = int(input("please enter age again:"))
# print("out of boundries, better luck next time!")

# 3
# num1 = int(input("please enter first number:"))
# num2 = int(input("please enter second number:"))
# while (num1%2 == 0) and (num2%2 == 0):
#     print(num1+num2)
#     num1 = int(input("please enter first number again:"))
#     num2 = int(input("please enter second number again:"))
# print(num1*num2)
# print("end of session, thank you ;)")

# 4
# num1 = int(input("please enter first number:"))
# num2 = int(input("please enter second number:"))
# while num1 + num2 == 10:
#     print("good job:)")
#     num1 = int(input("please enter first number again:"))
#     num2 = int(input("please enter second number again:"))
# print("wrond answer!, end of session :(")

# 5
# day = input("please enter day:")
# month = input("please enter month:")
# year = input("please enter year:")
# while 1<=day<=31 and 1<=month<=12 and 1950<=year<=2025:
#     if day < 10:
#         day = "0"+day
#     if month < 10:
#         month = "0"+month
#     if 2000<=year<=2009:
#         year = "0"+year%100

#=============================================

#HW 7.4
#print
#1
# sum = 0
# for i in range(6):
#     num = int(input("enter number:"))
#     sum = sum+num
# print(sum,sum/6 )

#2
# i = 0
# sum2 = 0
# sum = 0
# counter = 0
# for i in range(6):
#     num = int(input("enter number:"))
#     if num%2==0:
#         counter += 1
#         sum += num
        # sum2 = num

# print(sum,sum/counter)

#3
# i = 0
# for i in range(10,100):
#     if i%10 == 7:
#         print(i)

#4
# i = 0
# sum = 0
# for i in range(10,100):
#     if i%10 == 0:
#         sum += i
# print(sum)

#5

# grade = 0
# sum = 0
# counter = 0
# while 0<=grade<=100:
#     grade = int(input("please enter grade:"))
#     if grade>=60 and grade<=100:
#         sum+=grade
#         counter+=1
# print("the avarage is:",sum/counter)
# print("invalid grade better luck next time!")


#6
# grade = 0
# sum_p = 0
# sum_f = 0
# counter_p = 0
# counter_f = 0
# while 0<=grade<=100:
#     grade = int(input("please enter grade:"))
#     if 60<=grade<=100:
#         sum_p+=grade
#         counter_p += 1
#     if 0<=grade and grade<60:
#         sum_f+=grade
#         counter_f +=1
# if grade<0 or grade>100:
#     print(sum_p / counter_p , sum_f / counter_f)
#     print("invalid grade better luck next time!")



#6- ohad
# sum = 0
# sum1 = 0
# counter = 0
# counter1 = 0
# grade = 0

# while 0<=grade<=100:
#     grade = int(input("enter grade:"))
#     if grade>=60 and grade<=100:
#         sum+=grade
#         counter+=1
#
#     if grade<60:
#         sum1+=grade
#         counter1+=1
# print(sum / counter, "avarage of pass")
# print(sum1/counter1, "avarage of fail")
# if grade<0 or grade>100:
#     print("invalid grade fuck you!")

#7
# i = 0
# sum = 0
# for i in range(5):
#     i = int(input("please enter number here:"))
#     i = i%10
#     sum += i
# print(sum)


#8
# i = 0
# num = 0
# counter = 0
# num = int(input("please enter number:"))
# for i in range(1,num+1):
#     if i%5 == 0:
#         counter+=5
#         print(counter)


#9
# i = 0
# num = 0
# counter = 0
# num = int(input("please enter number here:"))
# for i in range(2,num+1):
#     if i%2 == 0:
#         counter+=2
#         print(counter)


#10
# num = 1
# counter = 0
# while num!=0:
#     num = int(input("please enter number:"))
#
#     if num%7==0 or num%3==0:
#         counter+=1
# print("wrong number!###",counter-1,"numbers from the list are divided by 3 and 7")


#1s
# i = 0
# sum = 0
# num = 0
# for i in range(6):
#     num = int(input("please enter number:"))
#     sum += num
#     avg = sum/6
# print(f"the avarage is: {avg}")

#2s
# i = 0
# sum = 0
# num = 0
# avg = 0
# counter = 0
# for i in range(6):
#     num = int(input("please enter number:"))
#     if num%2==0:
#         sum+=num
#         counter +=1
#         avg = sum/counter
# print(f"the avarage of the zugiim numbers is:{avg}")

#3s
# i = 0
# for i in range(10,100):
#     if i%10==7:
#         print(i)


#4s
# i = 0
# sum = 0
# for i in range(10,100):
#     if i%10==0:
#         sum+=i
# print(sum)

#5s
# grade = 0
# sum = 0
# counter = 0
# avg = 0
# while 0<=grade and grade<=100:
#     grade = int(input("please enter  grade:"))
#     if grade>=60 and grade<=100:
#         sum+=grade
#         counter+=1
#         avg = sum/counter
# print("invalid grade")
# print (f"the avarage of your grades is:{avg}")


#6s
# grade = 0
# sump = 0
# sumf = 0
# counterp = 0
# counterf = 0
# avgp = 0
# avgf = 0
# while grade>=0 and grade<=100:
#     grade = int(input("please enter grade:"))
#     if grade>=60 and grade<=100:
#         sump+=grade
#         counterp+=1
#         avgp = sump/counterp
#     if grade <60:
#         sumf+=grade
#         counterf+=1
#         avgf = sumf/counterf
# print("invalid grade!")
# print(f"the avarage of passed grades is:{avgp}")
# print(f"the avarage of failed grades is:{avgf}")


#7s
# i = 0
# num = 0
# sum = 0
# all = 0
# for i in range (5):
#     num= int(input("please enter number:"))
#     sum = num%10
#     all +=sum
# print(all)

#8s
# i = 0
# num = 0
# counter = 0
# num =int(input("please enter number:"))
# for i in range(1,num+1):
#     if i%5==0:
#         counter+=5
#         print(counter)

#9s
# i = 0
# num = 0
# counter = 0
# num = int(input("please enter number:"))
# for i in range(2,num+1):
#     if i%2==0:
#         counter+=2
#         print(counter)

#10s
# num = 1
# counter = 0
#
# while num!=0:
#     num = int(input("enter number:"))
#     if num%7==0 or num%3==0:
#         counter+=1
# print(counter-1)

# num = 1
# counter = 0
# while num!=0:
#     num = int(input("please enter number:"))
#
#     if num%7==0 or num%3==0:
#         counter+=1
# print("wrong number!###",counter-1,"numbers from the list are divided by 3 and 7")


grade = 0
grade1 = 0
sum = 0
counter = 0
high = 0
grade = int(input("please enter number:"))
grade=grade1
while grade>=0 and grade<=100:
    grade = int(input("please enter number:"))
    sum += grade
    counter += 1
    if grade>grade1 and grade>=0 and grade<=100:
        grade1 = grade


print(f"the highest number is:{grade1}")
print(f"the avarage is:{sum/counter}")






