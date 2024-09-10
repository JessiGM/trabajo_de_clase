#función para ingresar productos en una lista y mostrarlos
def mercado():

    total_market = 0

    for _ in range(5):
        name = str(input("Ingrese el nombre del producto: "))
        price = int(input("Ingrese el precio del producto: "))
        type = str(input("Ingrese el tipo de producto: "))
        count = int(input("Ingrese la cantidad del producto: "))
        total = price*count

        productos = [name, price, type, count]

        print("Usted eligio ",name," por un valor de $",price," la unidad, tipo de producto: ",type,", cantidad: ",count," por un total de $",total)
        print() 

        total_market += total

    print("El total a pagar por todos los productos es: $",total_market)    

mercado()    


