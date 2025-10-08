# importando a biblioteca matematica

import math
import os 
os.system('cls')

#funcoes basicas
# raiz quadrada 

valor_01 = 9
valor_02 = 16

print (math.sqrt(valor_01))
print (math.sqrt(valor_02))

print("potencia ou exponenciacao")

print(math.pow(2,3))
print(math.pow(valor_01,valor_02))

semMach= 2**3
print(semMach)


print("arredondar para cima")
print(math.ceil(3.2))
print(math.ceil(-1.8))

print("arredondar para baixo")
print(math.floor(3.2))
print(math.floor(-1.8))

print("valor absoluto")

print(math.fabs(-10))
print(math.fabs(7.5))