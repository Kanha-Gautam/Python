def fact(a):
	p=1
	if a!=1:
		a=a-1
		p=fact(a)
	return a*p

k=fact(5)	
print(k*5)
