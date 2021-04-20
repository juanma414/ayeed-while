#Se dispone de una serie de importes y para cada uno es necesario saber si se aplica o
#no un descuento. En caso afirmativo, calcular el importe del mismo. El criterio es el
#siguiente: para importes menores o iguales que 85, no se hace descuento y para
#importes mayores, se hace el 5 % de descuento. Informar cada importe (nunca cero)
#con su correspondiente descuento y, al final, el porcentaje que representa la cantidad
#de importes que tuvieron descuento, con respecto a la cantidad total de importes.

importe = float(input("ingrese el importe:"))
contA = 0
contB = 0
while importe != 0:
	if importe <= 85:
        contA = contA + 1
    else
        contB = contB + 1
        desc = importe * 0.05
        print ("el importe es:", importe)
        print ("el descuento es de:",desc)
importe = float(input("ingrese el importe:"))   
print("el porcentaje de la cantidad de importes que tuvieron descuento es:", (contB/(contB+contA)))  

