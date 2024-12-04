"""
1. Calcular precio y tipo en función de la edad y guardarlo para luego mostrarlo al usuario.[✅]

2. Pedir la edad[✅]
    Validar que sea entero positivo(Edad en positivo)[✅]
    Pedir edades hasta que se introduzca ""(Significa que ya son todos)[✅]

3. Calcular el precio total del grupo[✅]

4. Mostrar el precio total y el desglose por tipo de entrada
"""

#Valores globales
total_price = 0
group_people = []
tickets_type = ["Gratuita", "Niños", "Adultos", "Jubilados"]

#Solución con listas
ticket_accum = [0,0,0,0]
total_tickets = [0,0,0,0]
# FREE = 0
# KIDS = 1
# ADULTS = 2
# SENIOR = 3

def ticket_value_and_type(age: int) -> int:
    """
    Compresor que recibe una edad y calcula el precio del ticket
    de entrada al Zoo según el rango de edad.
    No valida que el imput sea correcto.
    """
    #Defino le precio de entrada
    ticket_price = 0
    ticket_type = 0
    #Calculo el precio según la edad
    #TODO: poner esta función para que los índices encajen con el resultado
    if age >= 3 and age <=12:
        ticket_price = 14
        ticket_type = 1
    elif age>= 13 and age < 65:
        ticket_price = 23
        ticket_type = 2
    elif age >= 65:
        ticket_price = 18
        ticket_type = 3
    
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
        break
    #Mientras me pasen el dato valido que sea entero positivo
    elif validates_int_positive(age):
       group_people.append(ticket_value_and_type(int(age)))

#Calcular precio total
num_tickets = len(group_people)
#Hacemos la iteración desestructurando la tupla
for ticket_price, ticket_type in group_people:

    total_price = total_price + ticket_price
    ticket_accum[ticket_type] += 1
    total_tickets[ticket_type] += ticket_price

#Con listas
for i, types in enumerate(tickets_type):
    print(f"{ticket_accum[i]:2d} entradas {types}: {ticket_price}")
   
print("--" * 25)

#Desglose: Como imprimir una "factura"
print(f"Número de entradas: {num_tickets:03d}")
print(f"Total a pagar ... : {total_price:.2f} Euros")