from flask import Flask, render_template, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "simon_game_secret"  # Nødvendig for sessionhåndtering

# Spil variabler
colors = ["red", "green", "blue", "yellow"]

def add_random_color():
    new_color = random.choice(colors)
    session["sequence"].append(new_color)

@app.route('/')
def index():
    # Start spillet hvis sekvensen ikke findes i session
    if "sequence" not in session:
        session["sequence"] = []
        session["player_sequence"] = []
        session["score"] = 0
        session["high_score"] = session.get("high_score", 0)
        add_random_color()

    # Hent den næste farve, spilleren skal trykke på
    if len(session["player_sequence"]) < len(session["sequence"]):
        next_color = session["sequence"][len(session["player_sequence"])]
    else:
        # Hvis spilleren har fuldført sekvensen, tilføjes en ny farve
        add_random_color()
        next_color = session["sequence"][-1]
    
    return render_template(
        'index.html', 
        next_color=next_color,  # Næste farve i sekvensen
        score=session["score"], 
        high_score=session["high_score"]
    )

@app.route('/player_input/<color>', methods=['POST'])
def player_input(color):
    # Tilføj spillerens input til sessionen
    session["player_sequence"].append(color)

    # Tjek spillerens sekvens mod den korrekte sekvens
    if session["player_sequence"] == session["sequence"][:len(session["player_sequence"])]:
        if len(session["player_sequence"]) == len(session["sequence"]):
            # Spilleren har gennemført sekvensen korrekt
            session["score"] += 1
            if session["score"] > session["high_score"]:
                session["high_score"] = session["score"]
            session["player_sequence"] = []  # Nulstil spillerens sekvens
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))
    else:
        # Spilleren har lavet en fejl - nulstil spillet
        session["sequence"] = []
        session["player_sequence"] = []
        session["score"] = 0
        add_random_color()  # Start ny sekvens
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
