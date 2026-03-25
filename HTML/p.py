# a=[10,20,30,40,50]
# if 10 and 30 in a :
#     print('correct')
# if 10 or 80 in a:
#     print('true')
# if 10 and 90 in a :
#     print('nothing')

# 1
# fruits = ['apple']
# fruits.append('mango')
# print(fruits)
# fruits.insert(2,'grapes')
# print(fruits)

# 2
# a = [10, 20, 30, 40, 50]
# a.remove(30)
# a.pop(3)
# print(a)

# 4
# a=[5,2,8]
# b=[3,7,1]
# a.extend(b)
# o=sorted(a) 
# print(o)
# a.extend(b)
# a.sort()
# print(a)

# 6
# From the list letters = ['a','b','c','d','e','f'],

# Print the first 3 elements

# Print the last 2 elements

# Print every 2nd element.

# letters = ['a','b','c','d','e','f']
# print(letters[:4])
# print(letters[4:6])
# print(letters[1:6:2])

# 7
# Reverse & Max/Min
# Given marks = [45, 67, 89, 23, 90, 56]
# Reverse the list
# Find the maximum and minimum marks.
# Given_marks = [45, 67, 89, 23, 90, 56]
# Given_marks.reverse()
# print(max(Given_marks),'is the maximum value')
# print(min(Given_marks),'is the minimum value')
# print(Given_marks)

# 8
# Nested Lists
# You have a matrix:
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# # Print the second row
# # Print all elements of the first column.
# print(matrix[1])
# for i in matrix:
#     print(i[0])

# 9
# Remove Duplicates
# Given nums = [1,2,3,2,4,1,5,3],
# # Write a program to remove duplicates and print a list with unique elements (order preserved).
# nums = [1,2,3,2,4,1,5,3]
# o=[]
# # print(list(set(nums)))

# for i in nums:
#     if i not in o:
#         o.append(i)
# print(o)


# def add(a, b):
#     c = a + b
#     print(c)        # just prints, not sending back

# result = add(10, 20) 
# add(3,5)
# add(8,2)


# a='ravi'
# print(a[::2])

# for j in range(97,123):
#     print(chr(j))


# ippudu okatuple undi andulo oka ele ni remove cheyali elano chudam
# q=(1,2,3,4)
# s=list(q)
# s.remove(2)
# q=tuple(s)
# print(tuple(q))


# s=[1,2,3,4,5]
# f=0
# for k in s:
#     f+=k
# print(f,'is  the total sum of the above list')


# def a(b,c=30):
#     b = 20
#     return b
# # a()
# print(a(b))
# ❓But question: "10 enduku ivvali mawa? already 20 chestham kada?"

# 👉 Answer:
# Python function lo b ane variable compulsory ga unnadhi, so function ni call chesthunna appudu Python cheptadi —

# “Nuvvu b ki value ivvali. Otherwise nenu start cheyanu.”

# Even though inside manam b=20 chestham, still starting lo value ivvali rule undi.


def a(b,c,d=10,e=15):
    b=30
    c=40
    print(b)
    print(c)
    return d , e
# print(a(30))
# print(a(40))
print(a(0,0,0,0))
