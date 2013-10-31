'''We can see that 28 is the first triangle number to have over five divisors.
 
What is the value of the first triangle number to have over five hundred divisors?
'''

def n_divisores(n):
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors
 
def triangular(limite):
    n = 1
    x, y = n_divisores(n), n_divisores(n+1)
    while x * y < 500:
        n += 1
        x, y = y, n_divisores(n+1)
    return n
 
index = triangular(500)
triangulo = (index * (index + 1)) / 2
 
print (triangulo)