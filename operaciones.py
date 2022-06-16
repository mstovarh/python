from cmath import e, log


n1 = int(input("Ingrese el primer numero\n"))
n2 = int(input("Ingrese el segundo numero\n"))

suma = n1+n2
resta = n2 - n1
prod = n1*n2
div = n1/n2
loga = log(n1,10)
pot1 = n1**n2
poteu = e**n1
raiz = n1**(1/n2)

print(f"\nSuma\t{suma} \nResta\t{resta} \nProducto\t{prod} \nCociente\t{div} \nLogaritmo\t{loga} \nPotencia\t{pot1} \nPotencia Euler\t{poteu} \nRaiz\t{raiz}")