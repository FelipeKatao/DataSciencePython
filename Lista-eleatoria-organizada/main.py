#Projeto 001:
#Criar uma Array 1X4 que seja gerada por numeros eleatorios diferentes e depois seja colocada em ordem.
#Ponto 1: A array tem que ter exatamente 4 posições
#Ponto 2: Os numeros devem ser diferentes
#Ponto 3: A Array deve ser retornada em ordem do maior para o menor


from random import *

NumRandom = randint(1, 10)
Array = [0, 0, 0, 0]
ArrayReserva = []
inx = 0
iny = 0
Loop =0

#Gerar uma array com numeros diferentes eleatorios#
while inx<=len(Array)-1:
  for n in Array:
    if int(n)==int(NumRandom):
      Loop=1
  if Loop==0:
    Array[inx]=NumRandom
    inx+=1
  else:
    NumRandom=randint(1,10)
    Loop=0
  NumRandom=randint(1,10)
  Loop=0
Array.sort()

print("Array criada com sucesso: "+str(Array))
