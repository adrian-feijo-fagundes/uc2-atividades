
print("Digite os 3 lados de um triângulo: ")

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

print(f"""
Primeiro lado: {lado1}
Segundo lado: {lado2}
Terceiro lado: {lado3}
""")


if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1 ):
  print ("Os valores forman um triângulo!")
  if lado1 == lado2 == lado3:
    print ("Eqilátero, 3 iguais")
  elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print ("isóceles, 2 iguais")
  else:
    print ("escaleno, 3 diferentes")
else:
  print("Não forma triângulo")

