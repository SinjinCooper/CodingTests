def collatz(n):
    if n == 1:
        return 0
    elif (n % 2) == 0:
        return 1 + collatz(n/2)
    else:
        return 1 + collatz((3*n) + 1)

num = input("Input a number: ")
print(collatz(int(num)))