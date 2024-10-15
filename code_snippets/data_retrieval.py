def retrieve_information(category, keywords, document):
    # Map categories to document fields
    category_fields = {
        "hotels": "hotels",
        "restaurants": "restaurants",
        "attractions": "attractions",
        "shopping": "shopping",
    }

    field = category_fields.get(category)
    if field:
        items = document.get(field)
        if items:
            # Filter items based on keywords if a specific item is requested
            specific_item = next((item for item in items if item['name'].lower() in keywords), None)
            if specific_item:
                return f"Here are the details for {specific_item['name']}:\n{specific_item['details']}"
            else:
                # List all items in the category
                item_list = "\n- ".join([item['name'] for item in items])
                return f"{category.capitalize()}:\n- {item_list}\n\nWould you like to learn more about a specific {category[:-1]}? If so, which one?"
    else:
        return "Sorry, I couldn't find any information for that category."
