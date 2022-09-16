# ex 173
def summ():

    x = input("Enter a number (blank to quit): ")
    if x == "":
        return 0
    else:
        return float(x) + summ()

print(summ())
