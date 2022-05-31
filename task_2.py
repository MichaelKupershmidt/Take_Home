#returns last 10 digits of a^b
def last(z):
	res = 1     
	x = z
	y = z

	x = x % 10000000000
	if (x == 0):
		return 0
	while (y > 0) :
		if ((y%2) == 1):
			res = (res * x) % 10000000000
		y = int(y/2)
		x = (x * x) % 10000000000
	return res
# driver code
# 
# 
# 
# 
answer = 1000
n=0
p=1
while p<(answer+1):
	n = n + last(p)
	n= n % 10000000000
	p+=1
print(n)
