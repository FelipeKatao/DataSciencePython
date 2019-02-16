import matplotlib.pyplot as plt

#Listas de onde serão extraida os dados
ValorX=[4,3,2,5,6]
Valory=[6,7,3,2,5]

ListaX2=[]
ListaY2=[]
#Função para colocar os valores para baixo
def ValorAbaixo(valorX,valorY):
  for x in ValorX:
    ListaX2.append(x-1)
  for y in valorY:
    ListaY2.append(y-1)
  pass

#Criação do grafico
fig,ax=plt.subplots()
ax.scatter(ValorX,Valory,facecolor="blue")
#ValorAbaixo(ValorX,Valory)
ax.scatter(ListaX2,ListaY2,facecolor="red")
ValorAbaixo(ValorX,Valory)
ax.scatter(ListaX2,ListaY2,facecolor="orange")

fig.savefig("Demostrativo_do_ano.png")