from flask import Flask,render_template
from Service import MainPageService

MainService = MainPageService.MainpageController()

app =Flask(__name__,template_folder="Template")

@app.route("/")
def initial():
    return render_template("index.html",Dominios=MainService.LerDominio(),Analise=MainService.LerAnalises())

if __name__ == "__main__":
    app.run(debug=True)