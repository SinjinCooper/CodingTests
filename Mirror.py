# Problem: from an array of digits, output the total number of digits
#   that create a mirror. The array [1, 3, 4, 3, 6] should output 3,  (3, 4, 3)
# Input: an array of digits (e.g. 1, 3, 4, 3, 6)
# Output: length of 

print("Enter a list of digits with a single space between each: ")
arr = input()

numArr = arr.split(' ')
numSet = set(numArr)

def find_mirrors():
    if len(numArr) == 1:
        return 1
    elif len(numSet) == len(arr.split(' ')):
        return "no mirror"
    else:
        return "dup exists continue dawg"

print(find_mirrors())