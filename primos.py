print("Algoritmo que determine si un número es divisible exacto entre otro número")
a=int(input("Ingresa el primer número: "))
b=int(input("Ingresa el segundo número: "))
if a%b==0:
	print("El número:",a, "es divisible exacto entre:",b,)
else:
	print("El número:",a, "no es divisible exacto entre:",b,)