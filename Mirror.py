# Takes an array of digits as input and returns mirros

print("Enter a list of digits with a single space between each: ")
arr = input()

numArr = arr.split(' ')
numSet = set(numArr)

def find_mirrors():
    if len(numArr) == 1:
        return 1
    elif if len(numSet) == len(arr.split(' ')):
        return "no mirror"
    else:
        return "dup exists continue dawg"

print(find_mirrors())