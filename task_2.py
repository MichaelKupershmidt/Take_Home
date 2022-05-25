#returns last 5 digits of a^b
#def last(a,b):




def calculate(endpoint, prevnum=0, n=0):
	if n == endpoint:
		if endpoint<6:
			return prevnum + n**n
		else:
			return prevnum + last(n,n)
	if n<6: #because before 6 there are no numbers with over 5 digits
		prevnum = prevnum + n**n
		return calculate(endpoint,prevnum,n+1)
	else:
		square = last(n,n)
		prevnum = (prevnum + square)%100000
		return calculate(endpoint,prevnum,n+1)

# driver code
# 
# 
# 
# 
answer = calculate(5)
print(answer)