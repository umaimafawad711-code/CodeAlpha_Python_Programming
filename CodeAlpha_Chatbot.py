
print("🤖 CodeAlpha Chatbot here! Type 'bye' to exit.")
while True:
    user = input("You: ").lower()
    if "hello" in user:
        print("Bot: Hi!")
    elif "how are you" in user:
        print("Bot: I'm great, Thank you!")
    elif "bye" in user:
        print("Bot: Goodbye! Have a nice day!")
        break
    else:
        print("Bot: Sorry, I didn’t understand that.")

