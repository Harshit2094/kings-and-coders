import requests
from flask import Flask

def get_hint(phrase):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }
    data = {
        "model": "gpt-3.5-turbo-16k-0613",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Give me a hint for the phrase. " + phrase}
        ],
        "max_tokens": 200,
        "temperature": 0,
        "top_p": 1,
        "frequency_penalty": 0.5,
        "presence_penalty": 0.5
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        if 'choices' in response_data:
            hint = response_data["choices"][0]["message"]["content"].strip()
            print("hint=",hint)
            return hint
        else:
            return "No hint available."
    else:
        return "Failed to fetch hint."

def generate_phrase():
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }
    data = {
        "model": "gpt-3.5-turbo-16k-0613",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Give me only a phrase or a word for a Hangman game. The phrase should not be too long."}
        ],
        "max_tokens": 50,
        "temperature": 0,
        "top_p": 1,
        "frequency_penalty": 0.5,
        "presence_penalty": 0.5
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        if 'choices' in response_data:
            phrase = response_data["choices"][0]["message"]["content"].strip()
            print(phrase)
            get_hint(phrase)
            return phrase 
        else:
            return "No phrase generated."
    else:
        return "Failed to generate phrase."

generate_phrase()
