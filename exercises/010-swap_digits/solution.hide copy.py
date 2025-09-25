# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  # Your code here
  aux = str(num)[1] + str(num)[0] 
  #convierto en texto (str) el numero(num) y cojo el rango[1] de la posicion que quiero
  # y luego lo concateno del reves, siendo la posicion 0 la primera y la 1 la segunda para
  #para que me salga el num del reves
  return int(aux)
   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(42))
