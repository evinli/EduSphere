import cohere

co = cohere.Client('81BT2ZiL7xz0oLKvb3NqzuG9xcCi5ERtAHM4EUtu')

def get_response(msg, chat_history):
    response = co.chat(msg,
                        model="command",
                        temperature=0.3,
                        chat_history=chat_history)
    return response.text



