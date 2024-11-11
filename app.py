from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Фразы для разных настроений
phrases = {
    "happy": ["Солнце светит, и мир полон возможностей!", "Сегодня отличный день!", "Улыбнись, жизнь прекрасна!"],
    "sad": ["Все проходит, и это тоже пройдет.", "Не бойтесь чувствовать грусть, она важна.", "Найди утешение в маленьких вещах."],
    "angry": ["Попробуй глубоко вдохнуть, прежде чем действовать.", "Постарайся найти спокойствие в хаосе.", "Выразите свои чувства, но делайте это мирно."],
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_phrase/<mood>')
def get_phrase(mood):
    phrase = random.choice(phrases.get(mood, ["Неизвестное настроение."]))
    return jsonify({"phrase": phrase})

if __name__ == '__main__':
    app.run(debug=True)
