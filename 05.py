"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

n = 2520
while  True:
	for i in range(1,21):
		x = n % i
		if x != 0:
			break
	if x == 0:
		break
	n += 20
print n