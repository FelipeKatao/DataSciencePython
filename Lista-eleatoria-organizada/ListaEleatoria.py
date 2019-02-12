from random import *


def CriarLista():
  NumRandom=randint(1,10)
  Array = [0,0,0,0]
  ArrayReserva=[]
  inx=0
  iny=0
  Loop=False
  while (len(Array) > inx):
    NumRandom = randint(1, 10)
    Array[inx] = NumRandom
    for n in Array:
      if Array[inx] == n:
         print(str(n) + " " + str(Array[inx]))
         NumRandom = randint(1, 10)
         Array[inx] = NumRandom
    print(Array)
    inx += 1
  print("Pronto")
