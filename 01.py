## If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.###
##The sum of these multiples is 23.###
##Find the sum of all the multiples of 3 or 5 below 1000##

soma_dos_multiplos = 0
for numeros_multiplos in range(1, 1000):
	if numeros_multiplos % 3 == 0 or numbers % 5 == 0:
		soma_dos_multiplos += numeros_multiplos
print soma_dos_multiplos