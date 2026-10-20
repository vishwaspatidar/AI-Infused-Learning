tools = [{
    "type": "function",                                      # ①
    "function": {
        "name": "get_price",                                 # ②
        "description": "Get the price of a shop item the user asks about.",  # ③
        "parameters": {                                       # ④
            "type": "object",
            "properties": {"item": {"type": "string", "description": "the item name"}},
            "required": ["item"],
        },
    },
}]