from db import *
from tool import *

# ① system personality — sets the bot's role for the whole conversation
SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are a friendly shop assistant for a clothing store. "
        "You help customers find prices, make recommendations, and remember "
        "what they've asked about earlier in the conversation."
    ),
}

conversation_history = []          # ② lives OUTSIDE agent() — persists across turns

def agent(user_message):
    # ③ add the new user message to history
    conversation_history.append({"role": "user", "content": user_message})

    # ④ build full message list: system + all history so far
    messages = [SYSTEM_PROMPT] + conversation_history

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b", messages=messages, tools=tools)
    msg = response.choices[0].message

    if msg.tool_calls:                                  # ⑤ tool call turn
        conversation_history.append(msg)               #    save assistant's tool-call msg
        tool_results = []
        for call in msg.tool_calls:
            args = json.loads(call.function.arguments)
            result = get_price(args["item"])
            print(f"   🔧 tool: get_price({args['item']}) → {result}")
            tool_results.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result,
            })
        conversation_history.extend(tool_results)      #    save tool results too

        # ⑥ second call so model turns tool results into a nice reply
        messages = [SYSTEM_PROMPT] + conversation_history
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b", messages=messages)
        msg = response.choices[0].message

    # ⑦ save the final assistant reply so future turns remember it
    conversation_history.append({"role": "assistant", "content": msg.content})
    return msg.content

while True:
    user_message = input("You: ")
    if user_message.strip().lower() in {"quit", "exit"}:
        break
    print("Bot:", agent(user_message))
    print(f"   (history: {len(conversation_history)} messages)")