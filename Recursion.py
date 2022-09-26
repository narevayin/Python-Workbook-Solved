# ex 173
# def summ():

#     x = input("Enter a number (blank to quit): ")
#     if x == "":
#         return 0
#     else:
#         return float(x) + summ()

# print(summ())

# ex 174

# def gcd(x , y):
#     if y == 0:
#         return x
#     else:
#         return gcd(y, x % y)

# print(gcd(65,15))

# ex 175

# def Binary(n):
#    if n > 1:
#        Binary(n//2)
#    print (n % 2,end = '')

# print(Binary(34))

# ex 178 

# def isPalindrome(s):
#     if len(s) <= 1:
#         return True
#     else:
#         return s[0] == s[len(s) - 1] and isPalindrome(s[1 : len(s) - 1])
# def main():

#     line = input("Введите строку: ")

#     if isPalindrome(line):
#         print("Palindrome")
#     else:
#         print("Not Palindrome")

# main()

# ex 180

# def distance(s, t):

#     if len(s) == 0:
#         return len(t)
#     elif len(t) == 0:
#         return len(s)
#     else:
#         cost = 0
#     if s[len(s) - 1] != t[len(t) - 1]:
#         cost = 1

#     d1 = distance(s[0 : len(s) - 1], t) + 1
#     d2 = distance(s, t[0 : len(t) - 1]) + 1
#     d3 = distance(s[0 : len(s) - 1] , t[0 : len(t) - 1]) +  cost

#     return min(d1, d2, d3)

# def main():

#  s1 = input("enter string: ")
#  s2 = input("enter string: ")

#  print( distance(s1, s2))
# main()
