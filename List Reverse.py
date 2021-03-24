'''
Author: Niel
Date: 22 March 2021
Purpose: Python Practice
'''

# to take a list as an imput from the user
lst = []
user = int(input("Enter number of elements:"))
for i in range(0,user):
    ele = int(input())
    lst.append(ele)

# by slicing method
a = lst[::-1]
#built in method
b = lst[:]
b.reverse()

#by using if statement
c = lst[:]
for i in range(0,len(c)//2):
    c[i], c[len(c) -i -1] = c[len(c) -i -1], c[i]

if c==b and b==a and a==c:
    print(f"All three methods give same result:\n{a}"
    f"\n{b}\n{c}")
