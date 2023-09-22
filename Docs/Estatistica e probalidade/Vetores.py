import math


class Vetor():
    def Somar_vetor(self, v, w):
        #Soma os vetores selecionados
        return [v_i + w_i for v_i, w_i in zip(v, w)]

    def SubtrairValores(self, v, w):
        #Subtrai os valores correspodente
        return [v_i - w_i for v_i, w_i in zip(v, w)]

    def Multiplicacao_escalar(self, z, c):
        #Um numero por Vetor
        return [c * v_i for v_i in z]

    def dot(self,v, w):
      #Retorna a multiplicação de vetor
        return sum(v_i * w_i for v_i, w_i in zip(v, w))

    def Soma_Quadrados(self, n):
      #Retorna a soma dos quadrados 
        return self.dot(n,n)

    def Magnetude(self,n):
      #Magnetude de um valor
        return math.sqrt(self.Soma_Quadrados(n))

    def distancia(self,v,w):
      #Distancia de um valor
      return self.Magnetude(self.SubtrairValores(v,w))
