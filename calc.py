def calc():
	exp = input("Enter the expression: ")
	spl = exp.find(" ")
	ope1 = exp[:spl]
	op = exp[spl+1]
	ope2 = exp[spl+3:]
	
	if(op == "+"):
		print(int(ope1)+int(ope2))
	elif(op == "-"):
		print(int(ope1)-int(ope2))
	elif(op == "*"):
		print(int(ope1)*int(ope2))
	elif(op == "/"):
		print(int(ope1)//int(ope2))
	if 'y' == input("Want to continue (y/n): "):
		calc()

calc()

