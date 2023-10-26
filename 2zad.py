import math
def three_n(n):
    for i in range(3*n):
        print(n)
        
def n_log_n(n):
    if n <= 0:
        return
    for j in range(int(n * math.log(n, 2))):
            print(n)

def factorial(n):
    if n > 0:
        for i in range(n):
            print(n)
        return(factorial(n-1))
    
def cub(n):
    if n <= 0:
        return
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(n)

def three_log_n(n):
    if n <= 0:
        return
    for i in range(3 * int(math.log(n, 2))):
        print(n)


