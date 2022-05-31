answer = 1000
n=0
p=1
while p<(answer+1):
	n = n + pow(p,p,10000000000)
	n= n % 10000000000
	p+=1
print(n)
