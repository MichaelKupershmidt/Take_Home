#returns last 5 digits of a^b
#def last(n):
# need to calulate eulers thoerm and get totient function
# also need to code gcd function and neew phi function
# solving for mod 100000 is a given and therfore not a parameter
# number is raised to itself therfore not a parameter 
# need to solve follwing equations/ implement functions:
# a^x mod m = a^(x mod t) mod m
# t = totient(m)
# gcd(a,b)=1
# φ(a)

def calculate(endpoint, prevnum=0, n=0):
	if n == endpoint:
		if endpoint<11:
			return prevnum + n**n
		else:
			return prevnum + last(n)
	if n<6: #because before 6 there are no numbers with over 5 digits
		prevnum = prevnum + n**n
		return calculate(endpoint,prevnum,n+1)
	else:
		square = last(n)
		prevnum = (prevnum + square)
		return calculate(endpoint,prevnum,n+1)

# driver code
# 
# 
# 
# 
answer = calculate(5)
print(answer)