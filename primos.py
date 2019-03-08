cont=0

a=int(input("ingrese un número: "))
for i in range(1,a+1,1):
	if a%i==0:
		cont=cont+1
	
if cont>2:
	print("no es número primo")
else:
	print("es un número primo")



