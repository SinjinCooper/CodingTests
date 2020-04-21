# A little function to test recursion. Drawing left aligned pyramid.

def draw(n):
    # base case
    if n == 0:
        return
    
    # recursive call to self
    draw(n-1)

    # print the as many symbols as n requires
    print("#"*n)

num = int(input("number: "))
draw(num)