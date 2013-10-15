import math
from math import log10

def digito(i,n):
	return n/(10**i)%10

def ndigitos(n):
	return int(log10(n))+1

def palindrome(n):
	k = ndigitos(n)
	for i in range(k/2):
		if digito(i,n) != digito(k - i -1 ,n):
			return False
	return True
print palindrome(123)
