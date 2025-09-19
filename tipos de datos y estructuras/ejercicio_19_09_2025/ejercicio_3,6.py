import random

#generar un número aleatorio (0 o 1) 
peatonal = random.randint(0, 1)

# estructura if/else para mostrar el mensaje
if peatonal == 1:
    print("El peatón puede cruzar.")
else:
    print("El peatón no puede cruzar.")
    