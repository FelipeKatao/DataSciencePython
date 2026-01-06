import dataalgo
import matplotlib.pyplot as plt
#analise de uum apanhado de dados#
#retornar um relatrio com grafico#

    #numero de Conexão por amigos
_conexao=[2,3,4,5,6,7,8,9,10,11,3,4,5,6,7]
_Dadosx=[10,45,23,67,12,47,12,45,89,12,34,68,93,12,45]
_quantil=[]
_quantilDeterminante=[]
_acuracia=[]

d=dataalgo.data()
d.Correlacao(_conexao,_Dadosx)
for x_i in _conexao:
  _quantil.append(d.derivada(x_i,0.4))
for x_i in _Dadosx:
  _quantilDeterminante.append(d.derivada(x_i,0.5))
  pass
x=0
while x<len(_conexao):
  _acuracia.append(d.Acurracia(_Dadosx,_Dadosx[x+1]))
  x+=1
  if x+1>=len(_conexao):
    break
pass

_acuracia.append(6)
print("tamanho:"+str(len(_acuracia)))
print("tamanho:"+str(len(_Dadosx)))
#Criação do grafico
fig,ax=plt.subplots()
ax.scatter(_conexao,_quantilDeterminante,facecolor="blue")
ax.scatter(_Dadosx,_acuracia,facecolor="red")

fig.savefig("Conexão com amigos.png")

