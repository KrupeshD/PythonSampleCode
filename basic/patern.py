num=input("Enter a Number: ")
n=int(num)
i=1
while i<=n:
	j=1
	while j<=i:
		print('*', end="")
		j=j+1
	i=i+1
	print('')
print('Done !')