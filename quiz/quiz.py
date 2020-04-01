# -*- coding: utf-8 -*-
# quiz/quiz.py

from flask import Flask
from flask import render_template

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
	SECRET_KEY='bardzosekretnysekret',
))

# lista pytań
DANE = [{
	'pytanie': 'Autor "Lalki" to:', #pytanie
	'odpowiedzi': ['Adam Mickiewicz', 'Juliusz Słowacki', 'Bolseław Prus'], #możliwe odp
	'odpok': 'Bolseław Prus'}, #poprawna odp
	{
	'pytanie': 'Stolica Polski to:',
	'odpowiedzi': ['Warszawa', 'Kraków', 'Gniezno'],
	'odpok': 'Warszawa'},
	{
	'pytanie': 'Stolica Hiszpani, to:',
    'odpowiedzi': ['Madryt', 'Warszawa', 'Barcelona'],
    'odpok': 'Madryt'},
    {
    'pytanie': 'Objętość sześcianu o boku 6 cm, wynosi:',
    'odpowiedzi': ['36', '216', '18'],
    'odpok': '216'},
    {
    'pytanie': 'Symbol pierwiastka Helu, to:',
    'odpowiedzi': ['Fe', 'H', 'He'],
    'odpok': 'He'},
    
]

@app.route('/')
def index():
    # return 'Cześć, tu Python!'
    return render_template('index.html', pytania=DANE)


if __name__ == '__main__':
    app.run(debug=True)