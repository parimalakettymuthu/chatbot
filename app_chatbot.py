# !pip install Flask
# !pip install --upgrade openai==0.28 

import subprocess
import sys 

def install(package):
  subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("Flask")
install("openai==0.28")

import openai
openai.api_key = ''

from flask import Flask, request, jsonify
import openai 

app = Flask(__name__)

@app.route('/chat/', methods=['POST'])
def chat(): 
  data = request.get_json()
  user_query = data.get('user_query')

  response = openai.ChatCompletion.create(
      model="gpt-4",
      messages = [
          {"role":"system", "content":"This is a chatbot that can converse on a wide range of topics."},
          {"role":"user", "content":user_query}
      ]
  )
  chatbot_response = response.choices[0].message['content']
  return jsonify({'response': chatbot_response})

  if __name__ == '__main__':
    app.run(debug=True)
    