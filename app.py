from flask import Flask, request, jsonify
from langchain_community.llms import Ollama

app = Flask(__name__)
llm = Ollama(model="gemma2")

@app.route('/query', methods=['POST'])
def query_ai():
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    response = llm.invoke(query)
    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(debug=True)
