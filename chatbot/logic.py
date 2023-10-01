import openai

with open('API_KEY', 'r') as file:
    api_key = file.read().strip()  

# Set the API key
openai.api_key = api_key

# Initialize messages with a system message
messages = []

def CustomChatGPT(user_input, selected_role):
    messages.append({"role": "system", "content": f"You are a {selected_role}. {user_input}"})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "user", "content": user_input})
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply
