cont=0
i=0
a=int(input("Ingrese un número: "))
while i<=a:
    i=i+1
    if a%i==0:
    	cont=cont+1
if cont>2:
	print("No es número primo")
else:
	print("Es número primo")
       
