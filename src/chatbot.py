import cohere

co = cohere.Client('81BT2ZiL7xz0oLKvb3NqzuG9xcCi5ERtAHM4EUtu')

chat_history = []
max_turns = 10

for _ in range(max_turns):
	# get user input
	message = input("Send the model a message: ")

	# generate a response with the current chat history
	response = co.chat(
		message,
		temperature=0.8,
		chat_history=chat_history
	)
	answer = response.text

	print("\n" + answer)

	# add message and answer to the chat history
	user_message = {"user_name": "User", "text": message}
	bot_message = {"user_name": "Chatbot", "text": answer}

	chat_history.append(user_message)
	chat_history.append(bot_message)