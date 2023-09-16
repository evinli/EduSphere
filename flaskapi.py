from flask import Flask
import src.translate as translate

app = Flask(__name__)

@app.get('/translate/<word>/<src>/<dest>')
def get_translation(word, src, dest):
    return translate.get_translation(word, src, dest)

@app.get('/languages')
def get_languages():
    return translate.get_all_languages()

if __name__ == '__main__':
    app.run()


