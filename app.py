from flask import Flask, render_template

app = Flask(__name__)

attractions = [
    {
        "id": 1,
        "name": "Sabrina Carpenter",
        "image": "sabrina_carpenter.jpg",
        "date": "15 de julho de 2025",
        "time": "20h",
        "lead_artist": "Sabrina Carpenter",
        "songs": ["Skinny Dipping", "Nonsense", "Vicious", "Busy Woman"],
        "description": "A estrela pop americana traz seu carisma e hits contagiantes para o palco principal do All Black Festival.",
        "comments": [
            {"author": "Ana Beatriz", "text": "Que voz incrível! Sabrina dominou o palco com muita energia e presença."}
        ]
    },
    {
        "id": 2,
        "name": "Jennie (BLACKPINK)",
        "image": "jennie.jpg",
        "date": "16 de julho de 2025",
        "time": "21h",
        "lead_artist": "Jennie",
        "songs": ["SOLO", "Play Me", "You & Me", "Like JENNIE", "Extra L"],
        "description": "Jennie apresenta um show solo repleto de estilo e performances incríveis no All Black Festival.",
        "comments": [
            {"author": "Bruno", "text": "Jennie foi sensacional! Um show cheio de energia e presença."}
        ]
    },
    {
        "id": 3,
        "name": "Stray Kids",
        "image": "stray_kids.jpg",
        "date": "17 de julho de 2025",
        "time": "22h",
        "lead_artist": "Stray Kids",
        "songs": ["MANIAC", "God’s Menu", "Thunderous"],
        "description": "Stray Kids traz um show enérgico, com coreografias e hits eletrizantes no All Black Festival.",
        "comments": [
            {"author": "Mariana", "text": "Incrível! A energia deles no palco foi incomparável."}
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', attractions=attractions)

@app.route('/attraction/<int:id>')
def attraction_details(id):
    attraction = next((item for item in attractions if item["id"] == id), None)
    return render_template('details.html', attraction=attraction)

if __name__ == '__main__':
    app.run(debug=True)
