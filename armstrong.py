x = int(input("Enter the number : "))
y = x
num = 0
while x>0:
	num+=(x%10)**3
	x = x//10
if num == y:
	print("Yes")
else:
	print("No")
