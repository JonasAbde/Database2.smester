from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"  # Denne route er for hovedsiden

@app.route('/figur')
def tegneseriefigur():
    return "Vakse Viggo"  # Denne route viser kun en simpel streng

@app.route('/figur/all')
def figure_all():
    print("Rendering myfirst.html")  # Print til debugging i terminalen
    return render_template('myfirst.html')  # Render HTML-filen 'myfirst.html'

if __name__ == '__main__':
    app.run(debug=True)  # Sørg for, at debug mode er aktiveret
