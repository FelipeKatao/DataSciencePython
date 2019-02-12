class Matriz():
  
    def Corpo(self, a):
        num_linhas = len(a)
        num_colunas = len(a[0]) if a else 0
        return num_linhas, num_colunas

    def Coletar_Linha(self, a, l):
        return a[l]

    def Coletar_coluna(self, a, c):
        return [a_i[c] for a_i in a]
