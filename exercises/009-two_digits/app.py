# Complete the function to return the tens digit and the units digit of any interger
def two_digits(numero_entero):

    if not (10 <= numero_entero <= 99):
        print("Error: El número debe ser un entero de dos dígitos (entre 10 y 99).")
        return None
    decenas = numero_entero // 10
    unidades = numero_entero % 10
    
    return (decenas, unidades)

# Invoke the function with any two digit integer as its argument
print(two_digits(79))

