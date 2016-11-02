temp=input("Enter Temperature in Celsius:")
try:
	cen=int(temp)
	feren=cen*(9/5)+32
	print("Temperature in Fahrenheit is",feren)
except:
	print("Please Enter Number")