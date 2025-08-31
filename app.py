from flask import Flask, render_template, request
import openai
import os   
from dotenv import load_dotenv

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = openai.Completion.create(
            model="gpt-5",
            prompt=user_input,
            max_tokens=100
        )
        return render_template("index.html", response=response.choices[0].text.strip)
    return render_template("index.html", response-None)

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    app.run(debug=True)