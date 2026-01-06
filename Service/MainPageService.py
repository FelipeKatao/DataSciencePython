import os
from flask import render_template_string

class MainpageController:
    def __init__(self):
        pass

    def LerDominio(self):
        arquivos = os.listdir("Data")
        Arquivos_filtrada = []
        for a in arquivos:
            Arquivos_filtrada.append(a.replace(".csv",""))
        return Arquivos_filtrada
    
    def LerAnalises(self):
        return render_template_string("<h1>Teste</h1>")