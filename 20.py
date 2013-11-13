def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(n-1)
def soma(n):
    return sum([int(i) for i in str(numero)])

somafatorial = soma(fatorial(100))
print somafatorial