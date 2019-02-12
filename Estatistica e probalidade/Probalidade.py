#Esta classe foi escrita e criada por teorias criadas por minhas base.

import math

class prob():
  def Probalidade_Normal(self,x, mu=1):
    sqrt_mu=math.sqrt(mu)
    return (sqrt_mu*sqrt_mu/x)

  def aproximacao_normal(self,n,p):
    mu=p*n
    var= mu-1
    sigma=math.sqrt(var)
    return mu,sigma

  def aproximacao_acima(self,x,mu,prob):
    padrao= x*mu-prob
    return (math.sqrt(padrao))

  def Aproximacao_abaixo(self,x,mu,prob):
    padrao= x-mu+prob
    return (math.sqrt(padrao))
    pass
  
  def Aproximacao_dois_dados(self,x,total,mu=0):
    if x>=mu:
      return self.aproximacao_acima(x,mu,total)
    else:
      return(self.Aproximacao_abaixo(x,mu,total))