# -*-coding: latin-1 -*-
""" Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""


soma_do_quadrado = sum([n**2 for n in range(1,100+1)])
print 'A soma dos quadrados dos primeiros dez números naturais é: %i' %(soma_do_quadrado)
soma = sum(range(1,100+1))
print 'O quadrado da soma dos primeiros cem números naturais é: %i' %(soma)

print 'A diferença dos primeiros 100 números natuaris e o quadrado da soma: %i ' %(soma_do_quadrado-soma)
