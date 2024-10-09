from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data til målinger
measurements = [
    {"lokation": "Vejle", "temp": 18, "tryk": 758, "dato": "10/9-2024"},
    {"lokation": "Varde", "temp": 16, "tryk": 754, "dato": "10/9-2024"},
    {"lokation": "Tårs", "temp": 16, "tryk": 762, "dato": "10/9-2024"},
    {"lokation": "Herning", "temp": 19, "tryk": 760, "dato": "10/9-2024"}
]

# Route til startsiden
@app.route('/')
def index():
    return render_template('index.html')

# Route til About siden
@app.route('/about')
def about():
    return render_template('about.html')

# Route til Målinger
@app.route('/measurements')
def measurements_page():
    return render_template('measurements.html', measurements=measurements)

# Route til Indtast Data siden
@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        lokation = request.form['lokation']
        temp = request.form['temp']
        tryk = request.form['tryk']
        dato = request.form['dato']
        # Tilføj den nye måling til listen
        measurements.append({"lokation": lokation, "temp": int(temp), "tryk": int(tryk), "dato": dato})
        return redirect(url_for('measurements_page'))
    return render_template('indtast.html')

if __name__ == '__main__':
    app.run(debug=True)
