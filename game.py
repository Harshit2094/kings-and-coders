import requests
from flask import Flask

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_KEY")

def get_hint(phrase):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo-16k-0613",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Give me a short, simple and vague hint to guess the word or phrase. " + phrase}
        ],
        "max_tokens": 500,
        "temperature": 1,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        hint = response_data["choices"][0]["message"]["content"].strip()
        print(hint)
        return hint 
    else:
        return "No phrase generated."

def generate_phrase():
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo-16k-0613",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Give me only a phrase or a word for a Hangman game. The phrase should not be too long. only write the word or phrase"}
        ],
        "max_tokens": 500,
        "temperature": 1,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        phrase = response_data["choices"][0]["message"]["content"].strip()
        print(phrase)
        return phrase 
    else:
        return "No phrase generated."

phrase=generate_phrase()
get_hint(phrase)