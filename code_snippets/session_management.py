from flask import session

def append_user_message(message):
    if 'chat_history' not in session:
        session['chat_history'] = []
    session['chat_history'].append(('user', message))

def append_chatbot_message(message):
    if 'chat_history' not in session:
        session['chat_history'] = []
    session['chat_history'].append(('chatbot', message))

def get_latest_chatbot_message():
    # Retrieve the last message sent by the chatbot
    chat_history = session.get('chat_history', [])
    for message_type, message in reversed(chat_history):
        if message_type == 'chatbot':
            return message
    return None
