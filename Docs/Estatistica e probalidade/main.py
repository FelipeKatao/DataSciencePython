from random import *
import Vetores as Vt
import Matrizes as Mt
import Graficos as Gf
import Estatistica as est
import Probalidade as prb
import Gradiente as grd

#Variaveis 
z = [12,34,56,7,8,2,10,43,21,67,8,9,3,4]
w = [2, 2, 2]
c = ['a', 'c', 'd']
v = ['d', 'b', 's']
zw = [[1, 2, 3], [4, 5, 6]]
ProbalidadeNormal=[]
ProbalidadeFinal=[]
NumRandom = randint(2, max(z))

Gard=grd.gradiente()
print(Gard.passos(z,w,3))

#Importar das Classes
VetorX = Vt.Vetor()
MatrizX= Mt.Matriz()
GraficoX= Gf.Graficos()
EstatiX=est.estatic()
ProbL=prb.prob()

#Criando uma probalidade acima ou abaixo
Media=EstatiX.Media(z)
print("O valor medio é:"+ str(Media))
print("O valor maximo é: "+ str(max(z)))
ProbalidadeFinal.append(ProbL.Aproximacao_dois_dados(NumRandom,max(z),Media))

print("Dado analizado: "+str(NumRandom))
NumRandom = randint(2, max(z))

ProbalidadeFinal.append(ProbL.Aproximacao_dois_dados(NumRandom,max(z),Media))

print("Dado analizado: "+str(NumRandom))
NumRandom = randint(2, max(z))

ProbalidadeFinal.append(ProbL.Aproximacao_dois_dados(NumRandom,max(z),Media))

print("Dado analizado: "+str(NumRandom))
NumRandom = randint(2, max(z))

ProbalidadeFinal.append(ProbL.Aproximacao_dois_dados(NumRandom,max(z),Media))

print("Dado analizado: "+str(NumRandom))
NumRandom = randint(2, max(z))

ProbalidadeFinal.append(ProbL.Aproximacao_dois_dados(NumRandom,max(z),Media))

print("Dado analizado: "+str(NumRandom))
NumRandom = randint(2, max(z))

ProbalidadeFinal.append(ProbL.Aproximacao_dois_dados(NumRandom,max(z),Media))

#Criação do Grafico
print("Pronto")
GraficoX.CriarGraficoBarras(ProbalidadeFinal,"Estatistica")
print("Grafico gerado com  sucesso")
