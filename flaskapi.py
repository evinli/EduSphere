from flask import Flask, request, jsonify
import src.translate as translate
import src.chatbot as chatbot

convo_history = []
app = Flask(__name__)

# Example: http://127.0.0.1:5000/translate?word=hello&src=english&dest=chinese%20(simplified)
@app.route('/translate', methods=['GET'])
def get_translation():
    word = request.args.get('word')
    src = request.args.get('src')
    dest = request.args.get('dest')
    translation = translate.get_translation(word, src, dest)
    jsonOutput = {"translation": translation}
    return jsonOutput

# Example: http://127.0.0.1:5000/languages
@app.route('/languages', methods=['GET'])
def get_languages():
    return jsonify(translate.get_all_languages())

# Example: http://127.0.0.1:5000/chatbot-query?msg=have%20a%20conversation%20with%20me%20in%20french,%20and%20subtely%20give%20me%20feedback%20on%20my%20responses
@app.route('/chatbot-query', methods=['GET'])
def chatbot_query():
    msg = request.args.get('msg')
    ans = chatbot.get_response(msg, convo_history)

    # Asd message and answer to the chat history
    user_message = {"user_name": "User", "text": msg}
    bot_message = {"user_name": "Chatbot", "text": ans}
    convo_history.append(user_message)
    convo_history.append(bot_message)

    jsonOutput = {"reply": ans}
    return jsonify(jsonOutput)

if __name__ == '__main__':
    app.run()


