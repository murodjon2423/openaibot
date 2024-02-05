import openai
openai.api_key = "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"

def chat_with_bot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_bot(user_input)
        print("Chatbot:", response)
