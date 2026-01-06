
class data():
  def media(self,x):
    totalx=len(x)
    somatorio=0;
    for x_i in x:
      somatorio+=x_i
    pass
    return somatorio/totalx
  def Quantil(self,porcent,x):
    return porcent*len(x) 
    pass
  def Correlacao(self,x,y):
    for x_i in x:
      x_i+=x_i
    for y_i in y:
      y_i+=y_i
    return x_i+y_i/len(x)-1
    pass
  def derivada(self,x,ponto):
    return x+ponto+1
    pass
  def Aoquadrado(x):
    return x*2
    pass
  def Acurracia(self,x,y):
    return x-y
    pass
  pass
