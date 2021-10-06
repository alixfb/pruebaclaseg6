totcompras = 0
compras = float(input("Digite el valor de la compra:"))
while compras!=0:
    if (compras < 0):
        compras = float(input("Digite nuevamente el valor de la compra:"))
    else:
        totcompras += compras
        compras = float(input("Digite el valor de otra compra:"))
print("El total de compras es:", totcompras)