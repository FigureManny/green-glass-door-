from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class GreenGlassDoorGame:
    def __init__(self):
        self.rules = ["Objects with double letters can pass through."]

    def can_pass(self, word):
        return any(letter*2 in word for letter in word)

game = GreenGlassDoorGame()

@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    return render_template('signup.html', username=username)

@app.route('/ggd')
def ggd():
    return render_template('GGD.html')

@app.route('/check', methods=['POST'])
def check():
    word = request.form.get('word', '')
    if game.can_pass(word):
        result = f'The word "{word}" can pass through the Green Glass Door!'
    else:
        result = f'The word "{word}" cannot pass through the Green Glass Door.'
    return render_template('GGD.html', result=result)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
