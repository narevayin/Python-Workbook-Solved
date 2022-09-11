# ex 113
# words = []
# word = input('enter word: ')
# while word != '':
#     if word not in words:
#         words.append(word)
#     word = input('enter word: ')
#     for word in words:
#         print (words)


# ex 114
# negatives = []
# zeros = []
# positives = []

# line = input("Enter an integer (blank to quit): ")
# while line != "":
#     num = int(line)
#     if num < 0:
#         negatives.append(num)
#     elif num > 0:
#         positives.append(num)
#     else:
#         zeros.append(num)

#     line = input("Enter an integer (blank to quit): ")

#     for n in negatives:
#         print(n)
#     for n in zeros:
#         print(n)
#     for n in positives:
#         print(n)



#ex115
# devisors = []
# number = int(input('enter number: '))
# for i in range (1, int(number/2)+ 1):
#     if number % i == 0:
#         devisors.append(i)
#         print (devisors)

# ex 116
# devisors = []
# number = int(input('enter number: '))
# for i in range (1, int(number/2)+ 1):
#     if number % i == 0:
#         devisors.append(i)
# print (devisors)

# print(sum(devisors) == number)

# ex 117
# text = 'python !$ te<,st'
# chars = '!@#$%^&*()_=-+><,.?/'
# for i in text:
#     if i in chars:
#         text = text.replace(i, '')
# print(text)


# ex 118

# res1 = []
# res2 = []
# text = input('Enter text: ')
# splits = text.split()
# for i in splits:
#     res1.append(i)
# for j in reversed(splits):
#     res2.append(j)
# print (res1 == res2)


# ex 119

# less = []
# more = []
# same = []
# mylist = [1, 7, 9, 144, 6, 2, 16]
# average = (sum(mylist)/len(mylist))
# for i in mylist:
#     if i < average:
#         less.append(i)
#     elif i == average:
#         same.append9i
#     else:
#         more.append(i)
# print ('Your average is ->', round(average))
# print (less, same, more)


# ex 120


# text = 'apples and oranges'
# text = text.replace(' and ', ', ')
# print(text)


# ex 121

# import random

# mylist = []
# while len(mylist) < 6:
#     random_number = random.randint(1,49)   
#     if random_number not in mylist:
#         mylist.append(random_number)     
# mylist.sort()
# print(mylist)

# ex 126
# import random
# player1 = []
# player2 = []
# player3 = []
# cards = []
# for suit in ["s", "h", "d", "c"]:
#     for value in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]:
#         cards.append(value + suit)

# random.shuffle(cards)

# while len(player1) < 5:
#     card = random.choice(cards)
#     cards.remove(card)
#     player1.append(card)
#     card2 = random.choice(cards)
#     cards.remove(card2)
#     player2.append(card2)
#     card3 = random.choice(cards)
#     cards.remove(card3)
#     player3.append(card3)

# print ('player1 has ', player1, '\n' 'player 2 has', player2, '\n' 'player3 has', player3)


# ex127

# x = [1, 5, 6, 8, 11, 17, 60]
# y = x.copy()
# y.sort()

# print (y == x)