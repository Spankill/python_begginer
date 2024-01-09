texto = input("ingresa un texto a tu elección:")

letras = []
texto = texto.lower()
letras.append(input("ingresa la primera letra: ").lower())
letras.append(input("ingresa la segunda letra: ").lower())
letras.append(input("ingresa la tercera letra: ").lower())

print("\n")
print("cantidad de letras")

cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")



print("\n")
print("cantidad de palabras")

palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")


print("\n")
print("letras de inicio y fin")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"la letra incial es '{letra_inicio}' y la letra final es '{letra_final}' ")


print("\n")
print("texto invertido")
palabras.reverse()
texto_invertido = ''.join(palabras)
print(f"si ordenamos tu texto al reves diria esto: {texto_invertido} ")


print("\n")
print("Buscando la palabra python")
buscar_python = 'python' in texto
dic = {True:"si",False:"no" }
print(f"La palabra 'python' {dic[buscar_python]} se encuentra en el texto insertado")





