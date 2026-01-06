from flask import Flask,render_template


app =Flask(__name__,template_folder="Template")

@app.route("/")
def initial():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)