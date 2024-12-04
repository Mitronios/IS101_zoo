#Con estructuras complejas:
"""
1. Calcular precio y tipo en función de la edad y guardarlo para luego mostrarlo al usuario.[✅]

2. Pedir la edad[✅]
    Validar que sea entero positivo(Edad en positivo)[✅]
    Pedir edades hasta que se introduzca ""(Significa que ya son todos)[✅]

3. Calcular el precio total del grupo[✅]

4. Mostrar el precio total y el desglose por tipo de entrada
"""

#Valores globales
group_people = []

#Diccionarios
ticket_menu = {
    "Gratuita": {"precio": 0, "e_umbral": 3},
    "Niños": {"precio": 14, "e_umbral": 13},
    "Adultos": {"precio": 23, "e_umbral": 65},
    "Jubilados": {"precio": 18, "e_umbral": float("inf")}
}

receipt = {
    "Gratuita": 0,
    "Niños": 0,
    "Adultos": 0,
    "Jubilados": 0
}

def ticket_value_and_type(age: int):
    #Defino le precio de entrada
    ticket_price = 0
    ticket_type = 0
    #Calculo el precio según la edad
    for ticket_type in ticket_menu:
        if age < ticket_menu[ticket_type]["e_umbral"]:
            ticket_price = ticket_menu[ticket_type]["precio"]
            break

    #Devuelvo el resultado
    return ticket_price, ticket_type

print(ticket_value_and_type(54)) 

#Valida que sea entero y positivo
def validates_int_positive(data: str) -> bool:
    """
    Predicado que recibe un dato del usuario y devuelve True si el dato es entero
    mayor o igual que 0.
    Devuelve False en caso contrario
    """
    #Respondo a voleo
    is_int_positive = False
    #Verifico que sea mayor un número positivo
    try:
        int(data)
        is_int_positive = True
    except:
        is_int_positive = False
    #Devuelvo el resultado
    return is_int_positive

#Calcular precio total
def total_price(group_list):
    """
    Calcula el precio total de las entradas
    """
    total = 0
    #Hacemos la iteración desestructurando la tupla
    for price, ticket_type in group_list:
        #Calculo el precio total
        total = total + price
        #Avanzo una posición
        receipt[ticket_type] = receipt[ticket_type] + 1
    return total

#Imprimir el desglose
def breakdown(receipt):
    for key in receipt:
        print(f"{receipt[key]:2d} entradas {key}: {receipt[key] * ticket_menu[key]['precio']:6.2f} €")
    print("--" * 25)
    num_tickets = sum(receipt.values())
    total_cost = total_price(group_people)
    #Desglose: Como imprimir una "factura"
    print(f"Número de entradas: {num_tickets:03d}")
    print(f"Total a pagar ... : {total_cost:.2f} Euros")
    return None


#Cuerpo del programa
"""
Bucle de repetición de edades, para cada edad debe imprimir precio y tipo
y acabar cuando se introduzca ""
"""
#Pedir edad 
while True:
    age = input("Cuántos años tienes?: ")
    #Si me pasan un campo vacío paro
    if age == "":
        breakdown(receipt)
        break
    #Mientras me pasen el dato valido que sea entero positivo
    elif validates_int_positive(age):
        ticket_price, ticket_type = ticket_value_and_type(int(age))
        group_people.append((ticket_price, ticket_type))
        #Actualiza la factura
        receipt[ticket_type] += 1
                
    



