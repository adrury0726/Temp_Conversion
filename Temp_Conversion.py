# temp convsersion

def menu():
	print("1. Celsius to Fahrenheit")
	print("2. Fahrenheit to Celsius")
	print("3. Exit")
	pick = int(input("Enter a choice:"))
	return pick
	
def toCelsius(f):
	return int((f-32) / (1.8))

def toFahrenheit(c):
		return int(c * 1.8 + 32)
	
def main():
	choice=menu()
	while choice != 3:
		if choice ==1:
			#convert C to F
			h = eval(input("75.5"))
			i = eval(input("32.0"))
			j = eval(input("-459.4"))
			k = eval(input("-40.0"))
			l = eval(input("0.0"))
			m = eval(input("100.0"))
			n = eval(input("212.0"))
			print =(str(toFahrenheit(h,i,j,k,l,m,n)))
			
		elif choice == 2:
			#convert F to C
			f = eval(input("75.5"))
			a = eval(input("32.0"))
			b = eval(input("-459.4"))
			c = eval(input("-40.0"))
			d = eval(input("0.0"))
			e = eval(input("100.0"))
			g = eval(input("212.0"))
			
			print =(str(toCelsius(a,b,c,d,e,f,g)))
		else	
			print("Invalid entry")
		choice== menu()	
			print(str(choice))
	
main()