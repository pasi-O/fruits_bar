import csrf
from flask import Flask, render_template, request
from data.fruits import fruit_facts
app = Flask(__name__)

@app.route('/')
def home():
    query = request.args.get('q', "").lower().strip()
    result = {}
    if query:
        for fruit in fruit_facts:
            if query in fruit.lower():
                result[fruit] = fruit_facts[fruit]
    else:
        result = fruit_facts

    return render_template("index.html",fruits=result)


if __name__ == "__main__":
    app.run(debug=True)