from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Bonjour"

@app.route("/french_to_english")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Hello"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
