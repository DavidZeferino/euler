def eprimo(n):
	divisor = 2
	while divisor < n:
		print n
		if n % divisor	== 0:
			yield False
		divisor += 1
	yield True

numero = 600851475143
fator =  numero - 1
while fator > 1:
	if numero % fator == 0 and eprimo(fator):
		break
	fator -= 1
print fator