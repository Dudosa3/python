a = input("Napis hodnotu a: ")
b = input("Napis hodnotu b: ")

max = a if a > b else b 
min = a if a < b else b 
if a == b:
	print("Obe hodnoty jsou stejne")
elif a == str:
	a = str
	print("Hodnota" , max , "je vetsi nez" , min)
elif a == float or int:
	a = float or int
	print("Hodnota", max, "je vetsi nez", min)
elif a == str and b == float or int:
	a == str and b == float or int
	print("Hodnota", max, "je vetsi nez", min)
	if a == float or int and b == str:
		a == float or int and b == str
		print("Hodnota", max, "je vetsi nez", min)


