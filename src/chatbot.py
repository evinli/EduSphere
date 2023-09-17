import cohere

co = cohere.Client('81BT2ZiL7xz0oLKvb3NqzuG9xcCi5ERtAHM4EUtu')

def get_response(msg, chat_history):
    if (msg is None):
        return "Please enter a message."
    response = co.chat(msg,
                        model="command",
                        temperature=0.3,
                        chat_history=chat_history)
    return response.text



