from model import chatbot

def main_bot():
    print('chatbot: hi how are you Abdelmasih how can I help You?')
    while True:
        user_input=input("User: ").lower()
        response=chatbot(user_input)
        print('chatbot: ',response)
        if user_input=="goodbye":
            break