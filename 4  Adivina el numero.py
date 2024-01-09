from random import randint


intentos = 0
numero_secreto = randint(1,100)
nombre = input("DIME TU NOMBRE: ")

print(f"Bueno, {nombre} , eh pensado un numero entre el 1 y 100\n Tienes 8 intentos para adivinar! SUERTE!")


while intentos<8:
    estimado = int(input("Cual es el Numero?:"))
    intentos += 1

    if estimado < numero_secreto:
        print("Mi numero es mas alto")

    if estimado > numero_secreto:
        print("Mi numero es mas bajo")
    if estimado == numero_secreto:
        print(f"FELICITACIONES !!! {nombre} !! ADIVINASTE EN {intentos} INTENTOS.")

        break

if estimado != numero_secreto:
    print(f" SIENTO DECIRTE QUE SE TERMINARON TUS INTENTOS. EL NUMERO SECRETO ERA: {numero_secreto} ")        
