# ex 38

# sides = int(input('enter number of sides: '))
# if sides == 3:
#     print ('it is a triangle')
# elif sides == 4:
#     print ('it is a square')
# elif sides == 5:
#     print ('it is a pentagon')
# elif sides == 6:
#     print ('it is a hexagon')
# elif sides == 7:
#     print ('it is a heptagon')
# elif sides == 8:
#     print ('it is a octagon')
# elif sides == 9:
#     print ('it is a nonagon')
# elif sides == 9:
#     print ('it is a decagon')
# else:
#     print ('error')


# # ex 39

# month = input('enter month: ')
# if month == 'december' or month == 'march' or month == 'may' or month == 'july' or month == 'august' or month == 'october' or month =='january':
#     print (month, 'has 31 days')
# elif month == 'february':
#     print (month, 'has 28 or 29 days')
# else: 
#     print (month, 'has 30 days')



# ex 40

# sound = int(input('enter dB level: '))
# if sound == 130: 
#     print (' it is a Jackhammer')
# elif sound == 106:
#     print (' it is a Gas Lawnmower')
# elif sound == 70:
#     print (' it is an Alarm Clock')
# elif sound == 40:
#     print (' it is a Quiet room')
# elif sound in range (106, 130):
#     print (' it is in between a Jackhammer and a Gas Lawnmower')
# elif sound in range(70, 106):
#     print (' it is in between an Alarm clock and a Gas Lawnmower')
# elif sound in range(40, 70):
#     print (' it is in between an Alarm clock and a Quiet Room')
# elif sound < 40:
#     print ('error')
# else:
#     print ('too high')


# ex 41

# side1= int(input('enter side 1: '))
# side2= int(input('enter side 2: '))
# side3= int(input('enter side 3: '))

# if side1 == side2 == side3:
#     print('triangle is an equilateral ')
# elif side1 != side2 and side1 != side3 and side2 != side3:
#     print ('triangle is a scalene')
# else:
#     print('triangle is an isosceles')

# ex42


# note = input('enter name')
# octave = int(input('enter octave'))

# C4_FREQ = 261,63
# D4_FREQ = 293,66
# E4_FREQ = 329,63
# F4_FREQ = 349,23
# G4_FREQ = 392,00
# A4_FREQ = 440,00
# B4_FREQ = 493,88

# if note == "C":
#     freq = C4_FREQ
# elif note == "D":
#     freq = D4_FREQ
# elif note == "E":
#     freq = E4_FREQ
# elif note == "F":
#     freq = F4_FREQ
# elif note == "G":
#     freq = G4_FREQ
# elif note == "A":
#     freq = A4_FREQ
# elif note == "B":
#     freq = B4_FREQ
# freq = freq / 2 ** (4 - octave)

# print("The frequency of", note, "is", freq)




# ex 44

# value = int(input('enter banknote value: '))
# if value == 1:
#     print ('George Washington')
# elif value == 2:
#     print ('Thomas Jefferson')
# elif value == 5:
#     print ('Abraham Lincoln')
# elif value == 10:
#     print ('Alexander Hamilton')
# elif value == 20:
#     print ('Andrew Jackson')
# elif value == 50:
#     print ('Ulysses S. Grant')
# elif value == 100:
#     print ('Benjamin Franklin')
# else:
#     print ('no such banknote exists.')

# ex 45

# date = input('enter date: ').title()
# if date == 'January 1':
#     print (date, 'is New Years day')
# elif date == 'July 1':
#     print (date, 'is Canada Day')
# elif date == 'December 25':
#     print (date, 'is Christmas Day')
# else: 
#     print ('no such holiday')


# ex 46 

# tile = input('enter tile: ')

# if tile[:1] == 'a' or tile[:1] == 'c' or tile[:1] == 'e' or tile[:1] == 'g':
#     print('colomn starts with black')
# else:
#     print('colomn starts with white')


# ex47

# month = input('enter month').title()
# day = int(input('enter day'))

# if month == 'April' or month == 'May':
#     print('it is spring')
# elif month == 'March' and day > 20:
#     print('it is spring')
# elif month == 'March' and day < 20:
#     print('it is winter')
# elif month == 'July' or month == 'August':
#     print('it is summer')
# elif month == 'June' and day > 21:
#     print('it is summer')
# elif month == 'June' and day < 21:
#     print('it is spring')
# elif month == 'October' or month == 'November':
#     print('it is fall')
# elif month == 'September' and day > 22:
#     print('it is fall')
# elif month == 'September' and day < 22:
#     print('it is summer')
# elif month == 'January' or month == 'February':
#     print('it is winter')
# elif month == 'December' and day > 21:
#     print('it is winter')
# elif month == 'December' and day < 21:
#     print('it is fall')
# else:
#     print ('error')
    

# ex48



# month = input('enter month: ').title()
# day = int(input('enter date: '))

# if month == 'December' and day >= 22:
#     print('your sign is a capricorn')
# elif month == 'January' and day <= 19:
#     print('your sign is a capricorn')
# elif month == 'January' and day >= 20:
#     print('your sign is an aquarius')
# elif month == 'February' and day <= 18:
#     print('your sign is an aquarius')
# elif month == 'February' and day >= 19:
#     print('your sign is a Pisces')
# elif month == 'March' and day <= 20:
#     print('your sign is a Pisces')
# elif month == 'March' and day >= 21:
#     print('your sign is a Aries')
# elif month == 'April' and day <= 19:
#     print('your sign is a Aries')
# elif month == 'April' and day >= 20:
#     print('your sign is a Taurus')
# elif month == 'May' and day <= 20:
#     print('your sign is a Taurus')
# elif month == 'May' and day >= 21:
#     print('your sign is a Gemini')
# elif month == 'June' and day <= 20:
#     print('your sign is a Gemini')
# elif month == 'June' and day >= 21:
#     print('your sign is a Cancer')
# elif month == 'July' and day <= 22:
#     print('your sign is a Cancer')
# elif month == 'July' and day >= 23:
#     print('your sign is a Leo')
# elif month == 'August' and day <= 22:
#     print('your sign is a Leo')
# elif month == 'August' and day >= 23:
#     print('your sign is a Virgo')
# elif month == 'September' and day <= 22:
#     print('your sign is a Virgo')
# elif month == 'September' and day >= 23:
#     print('your sign is a Libra')
# elif month == 'October' and day <= 22:
#     print('your sign is a Libra')
# elif month == 'October' and day >= 23:
#     print('your sign is a Scorpio')
# elif month == 'November' and day <= 21:
#     print('your sign is a Scorpio')
# elif month == 'November' and day >= 22:
#     print('your sign is a Sagittarius')
# elif month == 'December' and day <= 21:
#     print('your sign is a Sagittarius')
# else:
#     print('error')

# ex 49

# year = int(input('enter year: '))

# if year % 12 == 8:
#     print ('Dragon')
# elif year % 12 == 9:
#     print ('Snake')
# elif year % 12 == 10:
#     print ('Horse')
# elif year % 12 == 11:
#     print ('Sheep')
# elif year % 12 == 0:
#     print ('Monkey')
# elif year % 12 == 1:
#     print ('Rooster')
# elif year % 12 == 2:
#     print ('Dog')
# elif year % 12 == 3:
#     print ('Pig')
# elif year % 12 == 4:
#     print ('Rat')
# elif year % 12 == 5:
#     print ('Ox')
# elif year % 12 == 6:
#     print ('Tiger')
# elif year % 12 == 7:
#     print ('Hare')
# else:
#     print ('error')


# ex50

# mag = float(input('enter magnitude: '))

# if mag < 2.0:
#     print ('micro')
# elif mag > 2.0 and mag < 3.0:
#     print ('very minor')
# elif mag > 3.0 and mag < 4.0:
#     print ('minor')
# elif mag > 4.0 and mag < 5.03   :
#     print ('light')
# elif mag > 5.0 and mag < 6.0:
#     print ('moderate')
# elif mag > 6.0 and mag < 7.0:
#     print ('strong')
# elif mag > 7.0 and mag < 8.0:
#     print ('major')
# elif mag > 8.0 and mag < 10.0:
#     print ('Great')
# else:
#     print('meteoric')

# ex51

# x_value = float(input('The x value: '))
# y_value = float(input('The y value: '))
# z_value = float(input('The z value: '))
# discriminant = (y_value**2) - (4*x_value*z_value)
# if discriminant > 0:
#     print('Two Solutions. Discriminant value is:', discriminant)
# elif discriminant == 0:
#     print('One Solution. Discriminant value is:', discriminant)
# elif discriminant < 0:
#     print('No Real Solutions. Discriminant value is:', discriminant)

# ex52

# grade = input('enter letter: ')

# if grade == 'A+':
#     print('your grade is 4.0')
# elif grade == 'A':
#     print('your grade is 4.0')
# elif grade == 'A-':
#     print('your grade is 3.7')
# elif grade == 'B+':
#     print('your grade is 3.3')
# elif grade == 'B':
#     print('your grade is 3.0')
# elif grade == 'B-':
#     print('your grade is 2.7')
# elif grade == 'C+':
#     print('your grade is 2.3')
# elif grade == 'C':
#     print('your grade is 2.0')
# elif grade == 'C-':
#     print('your grade is 1.7')
# elif grade == 'D+':
#     print('your grade is 1.3')
# elif grade == 'D':
#     print('your grade is 1.0')
# elif grade == 'F':
#     print('your grade is 0')
# else:
#     print('error')



# ex53

# grade = float(input('enter your grade: '))

# if grade >= 4.0:
#     print('Your grade is A+')
# elif grade == 3.7:
#     print ('A-')
# elif grade == 3.3:
#     print ('B+')
# elif grade == 3.0:
#     print ('B')
# elif grade == 2.7:
#     print ('B-')
# elif grade == 2.3:
#     print ('C+')
# elif grade == 2.0:
#     print ('C')
# elif grade == 1.7:
#     print ('C-')
# elif grade == 1.3:
#     print ('D+')
# elif grade == 1.0:
#     print ('D')
# elif grade == 0:
#     print ('F')
# else:
#     print ('invalid')


# ex 54

# number = float(input('enter rate'))

# if number == 0.4:
#     print (f'{number * 2400}, Acceptable Performance')
# elif number >= 0.6:
#     print (f'{number * 2400}, Meritorious Performance')
# else:
#     print ('Unacceptable Performance')


# ex 55

# number = int(input('enter wavelength: '))

# if number in range (380, 450):
#     print ('violet')
# elif number in range (450, 495):
#     print ('blue')
# elif number in range (495, 570):
#     print ('green')
# elif number in range (570, 590):
#     print ('yellow')
# elif number in range (590, 620):
#     print ('orange')
# elif number in range (620, 750):
#     print ('red')
# else:
#     print ('out of range')

# ex 56

# x = float(input('enter waves: '))

# if x < 3*10**9:
#     print ('error')
# elif x > 3*1**9 and x < 3*10**12:
#     print ('Microwaves')
# elif x > 3*10**12 and x < 3*10**14:
#     print ('Infrared Light')
# elif x > 4.3*10**14 and x < 7.5*10**14:
#     print ('Visible Light')
# elif x > 7.5*10**14 and x < 3*10**17:
#     print ('Ultraviolet Light')
# elif x > 3*10**17 and x < 3*10**19:
#     print ('X-Rays')
# elif x > 3*10**19:
#     print ('Gamma Rays')
# else:
#     print ('error')

# ex 57

# min = int(input('enter minutes: '))
# sms = int(input('enter sms: '))

# if min > 50 and sms > 50:
#     print (f'{15.00}, {((min - 50) * 0.25) + (sms - 50) * 0.15}')    
# elif min > 50 and sms <= 50:
#     print (f'{15.00}, {((min - 50) * 0.25)}')    
# elif min <= 50 and sms > 50:
#     print (f'{15.00}, {((sms - 50) * 0.15)}')  
# elif min <= 50 and sms <= 50:
#     print ('15.00')

# ex58

# year = int(input('enter year: '))
# if year % 400 == 0:
#     print('leap')
# elif year % 100 == 0:
#     print('not leap')
# elif year % 4 == 0 and year % 100 != 0:
#     print('leap')
# else:
#     print('not leap')

# ex 59

# year = int(input("Input a year: "))

# if (year % 400 == 0):
#     leap_year = True
# elif (year % 100 == 0):
#     leap_year = False
# elif (year % 4 == 0):
#     leap_year = True
# else:
#     leap_year = False

# month = int(input("Input a month: "))

# if month in (1, 3, 5, 7, 8, 10, 12):
#     month_length = 31
# elif month == 2:
#     if leap_year:
#         month_length = 29
#     else:
#         month_length = 28
# else:
#     month_length = 30


# day = int(input("Input a day: "))

# if day < month_length:
#     day += 1
# else:
#     day = 1
#     if month == 12:
#         month = 1
#         year += 1
#     else:
#         month += 1
# print("The next date is ",  year,("-"),month,("-"),day)

# ex 60

# import math
# year = int(input('enter year: '))

# day_of_the_week = (year + math.floor((year - 1) / 4) - math.floor((year - 1) / 100) +
# math.floor((year - 1) / 400)) % 7

# if day_of_the_week == 0:
#     print ('Sunday')
# elif day_of_the_week == 1:
#     print ('Monday')
# elif day_of_the_week == 2:
#     print ('Tuesday')
# elif day_of_the_week == 3:
#     print('Wednesday')
# elif day_of_the_week == 4:
#     print('Thursday')
# elif day_of_the_week == 5:
#     print('Friday')
# elif day_of_the_week == 6:
#     print('Saturday')

# import random

# ex 62

# number = random.randrange(0,38)

# if number % 2 == 0 and number <= 18:
#     print (f'("The spin resulted in") {number}\n("Pay") {number}\n("Pay black")\n("Pay Even)\n("Pay 0 to 18")')
# elif number % 2 == 0 and number >= 19 and number != 38:
#     print (f'("The spin resulted in") {number}\n("Pay") {number}\n("Pay black")\n("Pay Even)\n("Pay 19 to 36")')
# elif number % 2 != 0 and number <= 18 :
#     print (f'("The spin resulted in") {number}\n("Pay") {number}\n("Pay red")\n("Pay odd)\n("Pay 0 to 18")')   
# elif number % 2 != 0 and number >= 19 and number != 37:
#     print (f'("The spin resulted in") {number}\n("Pay") {number}\n("Pay red")\n("Pay odd)\n("Pay 19 to 36")')   
# elif number == 37:
#     print ('pay 0')
# elif number == 38:
#     print ('pay 00')