# import math 
# ex 85

# def tri():
#     a = int(input('enter side: '))
#     b = int(input('enter side: '))
#     return round(math.sqrt(a**2 + b ** 2), 2)

# print(tri())

# ex 86

# def taxi():
#     distance = int(input('enter the distance: '))
#     price = distance/140 * 0.25
#     return 4.0 + price

# print(taxi())

# ex 87

# def total():
#     quantity = int(input('enter quantity'))
#     if quantity == 1:
#         return print('$10,95')
#     else:
#         return print(f'{10.95 + quantity*2.95} $') 

    
# total()


# ex 88

# def med():
#     mylist = []
#     mylist.append(int(input('enter number: ')))
#     mylist.append(int(input('enter number: ')))
#     mylist.append(int(input('enter number: ')))
#     mylist.sort()
#     return mylist[1]

# print(med())

# ex 89
# def numb():
#     n = int(input('enter number: '))
#     if n == 1:
#         print('first')
#     elif n == 2:
#         print('second')
#     elif n == 3:
#         print('third')
#     elif n == 4:
#         print('forth')
#     elif n == 5:
#         print('fifth')
#     elif n == 6:
#         print('sixth')
#     elif n == 7:
#         print('seventh')
    
# numb()


# ex 90
# def func():
#     s = input('enter word')
#     w = int(input('enter length '))
#     if len(s) >= w:
#         print (s)
#     else:
#         q = (w -len(s)) // 2
#         length = q * ' '
#         print (length, s )
# func()

# ex 94
# def tri():
#     mylist = []
#     mylist.append(int(input('enter side: ')))
#     mylist.append(int(input('enter side: ')))
#     mylist.append(int(input('enter side: ')))
#     mylist.sort()
#     return mylist[2] <= mylist[1] + mylist[0]
# print(tri())
    

# ex 96
# def integer():
#     x = input('enter: ')
#     if x[0] == '+' or x[0] == '-' and x[1 :].isdigit():
#         return 'int'
#     elif x[0 :].isdigit():
#         return 'int'
#     else:
#         return 'not int'

# print(integer())
        

# ex97

# def math():
#     x = input('enter: ')
#     if '+' in x or '-' in x:
#         return('1')
#     elif '*' in x or '/' in x:
#         return('2')
#     elif '^' in x:
#         return ('3')
#     else:
#         return ('-1')
# print(math())

# ex98


# def isPrime():
#     x = int(input('number: '))
#     if x <= 1:
#         return 'not prime'
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True
         
# ex99

# def isPrime():
#     x = int(input('number: '))
#     if x <= 1:
#         return 'not prime'
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     x += 1
    
#     if x % i == 0:
#         print(f'next prime is , {x}')
    
            

# isPrime()

# ex100

# from random import randint
# minm = 7
# maxm = 10
# asciin = 33
# asciim = 126
# def randomPassword():
#     randomLength = randint(minm, maxm)
#     result = ""
#     for i in range(randomLength):
#         randomChar = chr(randint(asciin, asciim))
#         result = result + randomChar
        
#     return result
# print(randomPassword())

# ex 101
# import random
# def licence():
#     chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     nums = '0123456789'
#     letters = ''
#     numbers = ''
#     for c in range(3):
#         letters += random.choice(chars)
        
#     for c in range(4):
#         numbers += random.choice(nums)

#     print (numbers, letters)

# licence()

# ex 102

# def security():
#     x = input('enter password')
#     upper = False
#     lower = False
#     number = False
#     upcase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     lowcase ='abcdefghijklmnopqrstuvwxyz'
#     nums = '1234567890'
#     for i in x:
#         if i in upcase:
#             upper = True
#         elif i in lowcase:
#             lower = True
#         elif i in nums:
#             number = True
    
#     if len(x) >= 8 and upper == True and lower == True and number == True:
#         print('Secure')
#     else:
#         print ('Not secure')
# security()

# ex 105
def isleap():
    year = int(input('enter year: '))
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def days():
    month = input("enter month: ")
    x = [1,3,5,7,8, 10, 12]
    y = [4,6,9,11]

    
    if month in x:
        print ('30 days')
    elif month in y:
        print ('31 days')
    elif isleap()== True and month == 2:
        print('29 days')
    elif isleap() == False and month == 2:
        print('28 days')

days()