# bot 
def get_response(user_input):
    text = user_input.lower()
    
    if "hello" in text or "hi" in text:
        return "Hi!"
    elif "how are you" in text:
        return "I'm fine, thanks!"
    elif "bye" in text or "exit" in text:
        return "Goodbye!"
    else:
        return "Tell me more."

print("Chatbot running (type 'bye' to exit)")

while True:
    user = input("You: ")
    bot = get_response(user)
    print("Bot:", bot)
    
    if "bye" in user.lower():
        break