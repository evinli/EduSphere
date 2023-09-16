from flask import Flask, request
import src.translate as translate

app = Flask(__name__)

# How to create flask query with request params
# Example: http://127.0.0.1:5000/translate?word=hello&src=english&dest=chinese%20(simplified)
@app.route('/translate', methods=['GET'])
def get_translation():
    word = request.args.get('word')
    src = request.args.get('src')
    dest = request.args.get('dest')
    return translate.get_translation(word, src, dest)

# j
@app.route('/languages', methods=['GET'])
def get_languages():
    return translate.get_all_languages()


if __name__ == '__main__':
    app.run()


