from flask import Flask, render_template

app = Flask(__name__)

# Route for startsiden, der linker til undersiderne
@app.route('/')
def opg2():
    return render_template('opg2lek6.html')

# Route for at vise alle bøger i en tabel
@app.route('/opg2/books')
def allbooks():
    return render_template('allbooks.html')

# Route for kun at vise bogtitler
@app.route('/opg2/bogtitler')
def bogtitler():
    return render_template('bogtitler.html')

if __name__ == '__main__':
    app.run(debug=True)
