Calculate Fibonacci Sequence

def Fib(endnumber):
	a,b=0,1
	for i in range(endnumber):
		a,b=b,a+b
		print(a,b)

Calculate Fibonacci Numbers

def Fibyield(endnumber):
	a,b=0,1
	for i in range(endnumber):
		yield(a)
		a,b=b,a+b
