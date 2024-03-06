def addition(a,b):
	return a+b

def substraction(a,b):
	return a-b

def multiplication(a,b):
	return a*b

def divsion(a,b):
	return a/b

a=float(input("enter first number:"))
o=input("Add->1\nSub->2\nMulti->3\nDivision->4\nenter operation:")
b=float(input("enter second number:"))
if o=="1":
	print(addition(a,b))
elif o=="2":
	print(substraction(a,b))
elif o=="3":
	print(multiplication(a,b))
elif o=="4":
	print(divsion(a,b))
else:
	print("not valid input . . .")
