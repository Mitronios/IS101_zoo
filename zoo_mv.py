"""
Objetivo: 
    Desarrollar un programa que calcule el precio total del costo de la entrada
    para un grupo de visitantes a un zoológico basado en sus edades.
    Debe proporcionar un desglose de los precios por edad.

Reglas de precios:
    El programa debe solicitar las edades de los miembros del grupo
    uno por uno.
    La entrada de datos debe terminar cuando se introduzca una
    cadena vacía.

Validación:
    Asegúrate de que las edades ingresadas sean números enteros y
    positivos.

3. Cálculo del Precio:
    Calcula el precio total del grupo basado en las reglas de precios.
    Proporciona un desglose detallado del costo por cada rango de edad.


4. Salida de Datos:
    Al finalizar la entrada de datos, muestra el precio total del grupo.
    Muestra el desglose detallado de los precios por edad.

Tareas a realizar:
    -Calcular el precio de la entrada según la edad y el determinar de que tipo es:
        >Gratuita, niños, adultos o jubilados
    -Calcular el precio total por el grupo validando que sea entero positivo
        >Guardar el precio total y la lista de tipos de entrada del grupo
    -Mostrar el precio total y desglose según el tipo de entrada.
    -Pedir la edad
"""

#Cáculo de precio y asignación de tipo
def calculate_ticket_price(age: int)-> any:
    """
    Selector que calcula el precio de la entrada según la edad,
    recibe un número entero y devuelve un entero con el número y 
    un string asignandole el tipo segun el precio.
    """
#Defino los valores iniciales
    ticket_price = 0
    ticket_type = "Gratuita"
    #Compruebo cada caso y asigno el precio
    if   3 <= age <= 12:
        ticket_price = 14
        ticket_type = "Niños"
    elif 13 <= age <= 64 :
        ticket_price = 23
        ticket_type = "Adultos"
    elif age >= 65:
        ticket_price = 18
        ticket_type = "Jubilados"

    #Devuelvo el precio
    return ticket_price, ticket_type

#print(calculate_ticket_price(1))

#Calculo del precio total
def total_price(tickets: list)-> None:
    #inicio el resultado
    total = 0
    types = ""
    breakdown = {}
    #Itero la lista
    for ticket in tickets:
        #Hago la suma
        total = total + ticket[0]
    #Itero para los tipos
    for _, ticket_type in tickets:
        if ticket_type in breakdown:
            breakdown[ticket_type] += 1
        else:
            breakdown[ticket_type] = 1

    print("\nDesglose de Precios")
    for ticket_type, count in breakdown.items():
        print(f"{ticket_type}: {count} entradas")
    
    print(f"\nPrecio total del grupo: {total} euros")
    #Devuelvo None
    return None

#Programa principal
def main():
    #Defino el valor inicial
    tickets = []
    #Repito el ciclo en tanto el usuario me pase una edad
    while True:
        age_input = input("Introduce la edad del visitante (o presiona Enter para finalizar): ")
        if not age_input:
            break
        #Valido los tipos y me aseguro que sea entero y solo valores positivos
        if not age_input.isdigit() or int(age_input) < 0:
            print("Por favor, introduce una edad válida (entero positivo).")
            continue
        #Convierto input(str) a int
        age = int(age_input)
        #Voy guardando la información
        ticket_price, ticket_type = calculate_ticket_price(age)
        tickets.append((ticket_price, ticket_type))
    #Calculo el precio total
    if tickets:
        total_price(tickets)
    else:
        print("No se introdujeron edades válidas.")#Si no me pasan una edad válida

# Ejecutar el programa
if __name__ == "__main__":
    main()