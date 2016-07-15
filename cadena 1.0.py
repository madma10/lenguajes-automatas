abc= input("ingresa los valores del alfabeto separados por una ,:  ")
abc.split(",")
print ("Tu alfabeto es: ")
print (abc.split(","))
enum = int(input("ingresa el numerador que deseas multiplicar la cadena: "))
if enum == 0:
        print('Tu cadena = {E}')
elif enum == 1:
    print (abc.split(",")*1)
elif enum >= 2:
        print(abc.split(",")*enum)

    

