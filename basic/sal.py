def computepay(h,r):
	try:
		hours=int(h) # Convert string input into integer
		rate=int(r)
		if hours<=40:
			wages=hours*rate
		else:
			wages=(40*rate)+((hours-40)*(rate*1.5))
		return wages
	except:
		print("Please Enter Number MotherFucker. ! ")

h=input("Enter Hours:") # Take Hours
r=input("Enter Rate:")  # Take Rate
wages=computepay(h,r)
print("Your Wages: ",wages)

		
