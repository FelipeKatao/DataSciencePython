import Vetores as vtz
import math

class estatic():
  Vetor= vtz.Vetor()
  #Define a tendenddia central da array
  def TendednciaCentral(self,n):
    return sum(n) / len(n)
    
  def MediaAbsoluta(self,n):
    n_l=len(n)-1
    x=0
    mediano=0
    while n_l>=x:
      mediano= mediano+n[x]
      x+=1
      if x>=n_l+1:
        break
    return (mediano/n_l)
    pass

  def Media(self,n):
    v=len(n)
    sorterd_n=sorted(n)
    pontoCentral= v//2
    
    if v%2 ==1:
      #se for impar, retorna o valor do meio
      return sorterd_n[pontoCentral]
    else:
      #se for par, retorna a media dos valores do meio
      lo=pontoCentral -1 
      hi=pontoCentral
      return (sorterd_n[lo]+sorterd_n[hi])/2

  def Quantil(self,n,p):
    p_index= int(p*len(n))
    return sorted(n)[p_index]
  
  def Data_amplitude(self,z):
    return max(z) - min(z)

  def por_variante(self,z):
    x_bar= self.TendednciaCentral(z)
    return [x_i - x_bar for x_i in z]
  
  def Variante(self,z):
    n=len(z)
    desvio= self.por_variante(z)
    desvio= self.Vetor.Soma_Quadrados(desvio)
    return desvio/(n-1)

  def desvio_padrao(self,z):
    return math.sqrt(self.Variante(z))
 
