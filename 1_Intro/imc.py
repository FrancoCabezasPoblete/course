def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc


peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
