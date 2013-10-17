'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

def primo(N):
	i = 2
	while i < N/2:
		if N%i == 0:
			return False
		i += True

i =  2
n = 3

while i!= 10001:
	n += 2
	if primo(n):
		i +=1

      
print n
