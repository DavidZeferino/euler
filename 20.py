def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
def soma(n):
    return sum([int(i) for i in str(n)])

somafatorial = soma(fatorial(100))
print somafatorial