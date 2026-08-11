import random
import json
with open('data.json') as file:
    responses=json.load(file)
def chatbot(user_input:str)->str:
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])