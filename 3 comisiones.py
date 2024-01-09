nombre = input ("por favor dime tu nombre:")
ventas = int(input ("ingresa tus ventas totales del mes:"))


comision = round(ventas*13/100,2)


print(f"hola {nombre} , tus comisiones de este mes son de: Bs. {comision}" )