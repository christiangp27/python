
#uso de condicionales
#uso de bucles
   # -for
    #-while
    #-switch

#condicionales
#uso de if
# x=1000
# y=200
# if x>y:
#     print("x es mayor que y")

# a=20
# b=20
# if a==b:
#     print("a es igual a b")
# #uso de if-else


# if a<b:
#     print("a es menor que b")
# else:
#     print("a es mayor que b")

# #uso de if-elif-else
# if x<y:
#     print("x es menor que y")
# elif x==y:
#     print("x es igual a y")
# elif 2*x==y:
#     print("x es la mitad de y")
# else:
#     print("x es mayor que y")


# #1.1.4 if anidados
# a="azúl"
# b="rojo"
# # if a=="azúl":
# #     if b=="rojo":
# #         print("si mezclas los colores tienes purpura")

# if a="azul" and b=="rojo":
#     print("si mezclas los colores tienes purpura")


"""bucles"""
universidad="univalle"
#uso de for
for letra in universidad:
    print(letra)


mi_lista=[]
for numero in range (1,10):
    mi_lista.append(numero)
    print(mi_lista)
print(mi_lista)    


#uso del while

#este tipo de bucles evalua una serie de instrucciones mientras cumple una condición

j=10
while j<20:
    print(j)
    j=j+1


#uso de switch
x=50

match x:
    case 20:
        print("x es 20")
    case 10:
        print("x es 10")
    case 8:
        print("x es 8") 
    case _:
        print(f"caso por defecto x es este valor {x}")
            