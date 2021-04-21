#1
# str = input("enter word:")
# str_new = ""
# for i in range(len(str)-1):
#     print(str[i])
#     if i == "a":
#         continue
#     else:
#         str_new += i
# print(str_new)

#1ohad
# str=input('enter word:')
# str_new= ''
# for i in str:
#     if i.upper()!="A":
#         str_new=str_new+i
# print(str_new)

#2
# str = input("word:")
# for i in str:
#     print(f"{str[0]}{str[-1]}")


#3
# from random import randint
# name = input("enter name:")
# password = ""
# for i in range(6):
#     num = randint(0,len(name)-1)
#     digit = name[num]
#     password+=digit
#
# print(password)

#4
# word1= input("enter word 1: ")
# word2= input("enter word 2: ")
# word3 = ""
# count = 0
# for i in word1:
#     if i in word2 and i not in word3:
#         word3+=i
#
# print(len(word3))

#5
# word = input("enter word:")
# sen = input("enter sentece: ")
# loc = 0
# list= []
# for word1 in sen:
#     if word in sen:
#         ind = sen.find(word,loc)
#         if ind == -1:
#             break
#         loc = ind+1
#         list.append(ind)
#
# print(list)

#5#solution- orly
# sentence = input("enter sentence: ")
# word = input("enter word: ")
# list_index=[]
# start_search=0
#
# for i in range(sentence.count(word)):
#     word_loc=sentence.index(word,start_search)
#     start_search=word_loc+1
#     list_index.append(word_loc)
#
# print(list_index)
#

#6
# sen = input("enter sentence: ")
# list_sen = sen.split()
# list2 = []
# str = ""
# for i in list_sen:
#     list2.append(i.capitalize())
#
# for i in list2:
#     str+=(i)+" "
#
# print(str)

#7
# sen = input("enter sentence: ")
# letter = input("enter letter: ")
# list1 = []
# str = ""
# for i in sen:
#     if i == letter:
#         i = i.upper()
#         str+=i
#
#     else:
#         str+=i
# print(str)

#1
# word = input("enter word: ")
# str = ""
# for i in word:
#     if i == "a" or i == "A":
#         continue
#     else: str+=i
# print(str)

#2
# word = input("enter word: ")
#
# for i in word:
#     print(word[0]+word[-1])

#3
# from random import randint
# name = input("enter name: ")
# password = ""
# for i in range(6):
#     num = randint(0,len(name)-1)
#     digit = name[num]
#     password +=digit
# print(password)

#4
# word1 = input("enter word 1: ")
# word2 = input("enter word 2: ")
# count = 0
# list1 = []
# for i in word1:
#     if i in list1:
#         continue
#     if i in word2:
#         count+=1
#         list1+= i
#
# print(f"there are {count} letters similar")

#5
# word = input("enter word: ")
# sen = input("enter sentence: ")
# loc = ""
# for i in sen.count(word):
#     if word in sen:
#         word.loc +=sen.index(word,loc)
# print(loc)

#6
# sen = input("enter sentence: ")
# list1 = sen.split()
# list2 = []
# str1 = ""
# for i in list1:
#     list2.append(i.capitalize())
#
# for i in list2:
#     str1 += i+" "
# print(str1)


#7
# sen = input("enter sentence: ")
# letter = input("enter letter: ")
# str1 = ""
# for i in sen:
#     if i == letter:
#         i = i.capitalize()
#         str1+=i
#         continue
#     if i != letter:
#         str1+=i
# print(str1)

#internet 1.0
