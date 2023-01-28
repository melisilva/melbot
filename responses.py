import random

def get_response(message:str):
    p_message = message.lower()

    if p_message == "hello" or p_message == "hi" or p_message == "hey" or p_message == "holo":
        return "Holo"
    elif p_message == "how are you" or p_message == "how are you doing":
        return "I'm existing, how about you?"
    elif p_message == "!help":
        return "I'm a bot, I don't need help"
    
    return "I don't understand. Please repeat"
