import nltk
from nltk.chat.util import Chat, reflections

# Responses for the chatbot
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how can I (.*)", ["You can %1 by doing XYZ."]),
    (r"can you (.*)", ["Yes, I can %1."]),
    (r"where are you from?", ["I'm a chatbot, so I exist wherever you need me!"]),
    (r"who created you?", ["I was created by a developer using Python and NLTK."]),
    (r"when is your birthday?", ["I don't have a birthday. I'm here to help you anytime!"]),
    (r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!"]),
    (r"(.*) (location|city) (you|your)", ["I am just a program, I am everywhere!"]),
    (r"how old are you?", ["I don't have an age. I'm just here to assist!"]),
    (r"(.*) (weather|temperature) (.*)", ["I'm sorry, I don't have access to weather information."]),
    (r"(.*) (sport|game) (.*)", ["I'm not really into sports, but I can help you with information!"]),
    (r"who (.*) (player|personality) (.*)", ["I don't have access to that information, but I can help with general facts!"]),
]

# Create a chatbot with pairs and reflections
chatbot = Chat(pairs, reflections)

# Start chatting
def main():
    print("Hi, I'm ChatBot. How can I help you?")

    while True:
        user_input = input("You: ")
        print(f"Debug: User input received: {user_input}")  # Debugging print statement
        if user_input.lower() == 'quit':
            print("ChatBot: Bye, and Eat, Sleep, Code and Repeat!")
            break
        response = chatbot.respond(user_input)
        print(f"Debug: Chatbot response: {response}")  # Debugging print statement
        if response:
            print("ChatBot:", response)
        else:
            print("ChatBot: I'm sorry, I don't understand that.")

if __name__ == "__main__":
    print("Debug: Script is running")
    main()
