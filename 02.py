#Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
#By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.

numero, regra_fibonacci, soma_fibonacci = 1, 0, 0
while numero < 400:#0000#
	numero, regra_fibonacci = numero + regra_fibonacci, numero
	if  numero % 2 == 0:
        soma_fibonacci += numero
print soma_fibonacci