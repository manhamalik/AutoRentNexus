def get_information(user_input, chatbot_message):
    doc = nlp(user_input)
    keywords = [token.lemma_.lower() for token in doc]

    # Small talk fallbacks
    if any(token.lower_ in ["hi", "hello", "hey"] for token in doc):
        return "Hi there! I'm here to help you explore the world. Just type in a city name to get started."

    # Handling city input with synonyms and variations
    city_aliases = {
        "paris": ["paris", "city of lights"],
        "dubai": ["dubai", "dbx"],
        # ... other cities with their aliases ...
    }

    for city, aliases in city_aliases.items():
        if any(alias in keywords for alias in aliases):
            document_id = get_document_id_for_city(city)
            session['document_id'] = document_id
            return "Would you like to learn more about the hotels, restaurants, attractions, or shopping centers?"

    # Handling categories and specific inquiries
    # ... rest of the logic ...
