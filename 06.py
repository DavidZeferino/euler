# -*-coding: latin-1 -*-
""" Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""


soma_do_quadrado = sum([n**2 for n in range(1,100+1)])
print 'A soma dos quadrados dos primeiros dez n�meros naturais �: %i' %(soma_do_quadrado)
soma = sum(range(1,100+1))
print 'O quadrado da soma dos primeiros cem n�meros naturais �: %i' %(soma)

print 'A diferen�a dos primeiros 100 n�meros natuaris e o quadrado da soma: %i ' %(soma_do_quadrado-soma)
