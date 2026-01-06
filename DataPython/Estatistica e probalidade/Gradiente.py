class gradiente():

  def passos(self,v,direct,tamanho_passo):
    return [v_i+ tamanho_passo*direct_i
      for v_i, direct_i in zip(v,direct)]