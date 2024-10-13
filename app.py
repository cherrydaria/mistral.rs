from flask import Flask, render_template, request
from openai import OpenAI
import json

app = Flask(__name__)

client = OpenAI(api_key="foobar", base_url="http://localhost:8080/v1/")  #

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['user_input']  # Изменяем на request.json для работы с JSON
    response = client.chat.completions.create(
        model="mistral",
        messages=[{"role": "user", "content": user_input}],
        max_tokens=256,
        frequency_penalty=1.0,
        top_p=0.1,
        temperature=0,
    )
    assistant_response = response.choices[0].message.content
    return assistant_response

if __name__ == '__main__':
    app.run(debug=True)