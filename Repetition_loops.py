    
# ex 63
# x = [5, 10, 15, 20, 25]
# sum = 0
# for i in x:
#     sum = sum + i
# print (sum/len(x))

# ex64

# price = [4.95, 9.95, 14.95, 19.95, 24.95]
# for i in price:
#     print (round(i * 0.6, 2), i)

# ex 65
# for i in range(0, 100, 10):
#     print(i, (i * 1.8 + 32))

# ---


# for i in price:
#     if int(i * 100) % 5 == 0:
#         print (i)
#     elif (i * 100) % 5 < 4:
#         print(math.floor(i))
#     elif (i * 100) % 5 >= 4:
#         print(math.ceil(i))
        

# ex68

# grade = input('enter letters: ')


# for i in grade:
#     if i == 'A+':
#         print('your grade is 4.0')
#     elif i == 'A':
#         print('your grade is 4.0')
#     elif i == 'A-':
#         print('your grade is 3.7')
#     elif i == 'B+':
#         print('your grade is 3.3')
#     elif i == 'B':
#         print('your grade is 3.0')
#     elif i == 'B-':
#         print('your grade is 2.7')
#     elif i == 'C+':
#         print('your grade is 2.3')
#     elif i == 'C':
#         print('your grade is 2.0')
#     elif i == 'C-':
#         print('your grade is 1.7')
#     elif i == 'D+':
#         print('your grade is 1.3')
#     elif i == 'D':
#         print('your grade is 1.0')
#     elif i == 'F':
#         print('your grade is 0')

# # ex69

# sum = 0

# while True:
#    age = input("Please enter the age. If no more member available please press ENTER key: ")
#    if age == "":
#        break
#    else:
#        age = int(age)
#        if age < 2:
#            sum = sum + 0
#        elif age > 3 and age < 13:
#            sum = sum + 14
#        elif age > 14 and age < 65:
#            sum = sum + 23
#        else:
#            sum = sum + 18

# sum_total = "{:.2f}".format(sum)

# print("The total of your group is ",sum_total)

# ex72

# x = range(1, 101)
# for i in x:
#     if i % 3 == 0 and i % 5 != 0:
#         print (i, 'fizz')
#     elif i % 5 == 0 and i % 3 != 0:
#         print (i, 'buzz')
#     elif i % 5 == 0 and i % 3 == 0:
#         print (i, 'fizz-buzz')
#     else:
#         print (i)


# ex79


# n = int(input('enter number: '))
# m = int(input('enter number: '))
# d = 2

# while True:
#     if n % d == 0 and m % d == 0:
#         print (d)
#         break
#     else:
#         d += 1
#         if n % d == 0 and m % d == 0:
#             print (d)
#             break

# ex 81

# number = int(input('Enter number: '))
# s = ''
# while number != 1:
#     x = number % 2
#     s += str(x)
#     s += '|'
#     number = number // 2
# print('|' + str(number) + s[::-1] + '|')





# ex 83

# from random import randrange
# NUM_ITEMS = 100
# mx_value = randrange(1, NUM_ITEMS + 1)
# print(mx_value)
# num_updates = 0
# for i in range(1, NUM_ITEMS):
#     current = randrange(1, NUM_ITEMS + 1)
#     if current > mx_value:
#         mx_value = current
#         num_updates = num_updates + 1
#         print(current, "<== Update")
#     else:
#         print(current)
# print("The maximum value found was", mx_value)
# print("The maximum value was updated", num_updates, "times")











