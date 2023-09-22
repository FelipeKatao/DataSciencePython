import matplotlib as mpl
import numpy as np
mpl.use('Agg')
import matplotlib.pyplot as plt


class Graficos():
    def CriarGraficoBarras(self, z,Graficoname):
        y_axis = z
        x_axis = range(len(y_axis))
        width_n = 0.4
        bar_color = 'blue'
        plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
        plt.savefig(Graficoname+'.png')

    def CriarGraficoDispersao(self,z,w):
      plt.scatter(z,w)
      plt.savefig('Grafico.png')
    def CriarGraficoPizza(self,Parte1,Parte2):
      fig,eixos =plt.subplots(nrows=1, ncols=2, figsize=(8,4))
      pie_1 = eixos[0].pie(Parte1,Parte2,autopct='%1.1f%%', colors=['gold', 'lightskyblue'])
      plt.savefig('Grafico.png')