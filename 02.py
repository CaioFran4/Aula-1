#Crie um algoritmo que leia 3 valores referente (lados de um triângulo)
#Determine se formam um triângulo, e se formar verifique
#se é um equilátero, isósceles ou escaleno.

lado1 = float(input("Qual o valor do lado 1?"))
lado2 = float(input("Qual o valor do lado 2?"))
lado3 = float(input("Qual o valor do lado 3?"))

Triângulo = lado1 + lado2 > lado3 and lado1 + lado2 > lado3 and lado2 + lado3 > lado1

eq = (lado1 == lado2 == lado3)

isó = (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3)

if Triângulo:
    "Os valores formam um Triângulo"
else:
    "Os valores não formam um Triângulo"


if eq:
    Resultado = "É um Triângulo Equilátero"

elif isó:
    Resultado = "É um Triângulo Isósceles"

else:
    "É um Triângulo Escaleno"








print (f"Resultado: {Triângulo}")
print (f"Tipo de Triângulo: {Resultado}")


