import json
import os

from dotenv import load_dotenv, find_dotenv

import openai
from flask import Flask, redirect, render_template, request, url_for

from .src.openaifuncs import get_completion

# Load Environment Variables
_ = load_dotenv(find_dotenv())


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    """The route is set to both accept GET and POST requests to the root URL ("/").
    When a GET request is made, it renders an HTML template called "index.html" and
    passes the "result" parameter as None.

    When a POST request is made, the code extracts the value of the "animal" field
    from the submitted form data using the Flask "request" object. It then uses OpenAI's API
    to generate text based on the extracted animal prompt. The generated text is then
    redirected back to the index route with the result parameter set to the generated text.

    The index route then re-renders the HTML template with the updated "result"
    parameter value, which will display the generated text on the page."""

    # Load the communication chart
    with open("reference/comm_chart.json", "r") as fp:
        comm_chart = json.load(fp)

    if request.method == "POST":
        topic = request.form["topic"]
        channel = request.form["channel"]
        tone = request.form["tone"]
        persona = request.form["persona"]
        purpose = request.form["purpose"]
        language = request.form["language"]
        words = request.form["slider"]
        print(words)

        prompt = one_shot_prompt(
            topic=topic,
            channel=channel,
            persona=persona,
            tone=tone,
            purpose=purpose,
            words=words,
            language=language,
        )

        results = get_completion(prompt)
        resjson = json.loads(results)
        print(resjson)
        print(prompt)

        return render_template(
            "results.html",
            results=[resjson[x] for x in resjson.keys()],
            topic=topic,
            channels=[channel] + comm_chart["Channel"],
            personas=[persona] + comm_chart["Persona"],
            tones=[tone] + comm_chart["Tone"],
            purposes=[purpose] + comm_chart["Purpose"],
            languages=[language] + comm_chart["Language"],
        )

    elif request.method == "GET":
        results = request.args.get("results")  # None

        return render_template(
            "index.html",
            results=results,
            channels=comm_chart["Channel"],
            personas=comm_chart["Persona"],
            tones=comm_chart["Tone"],
            purposes=comm_chart["Purpose"],
            languages=comm_chart["Language"],
        )


@app.route("/results")
def results():
    return render_template("results.html")


@app.route("/about")
def about():
    return render_template("base.html")


@app.route("/redirect")
def redirect_to_main():
    return redirect(url_for("index"))


@app.route("/login")
def login():
    return render_template("base.html")


def one_shot_prompt(
    topic=None,
    channel=None,
    persona=None,
    tone=None,
    purpose=None,
    words=None,
    language=None,
):
    prompt = f"""

    You are copywriter for a digital marketing agency. You are asked
    to write three post for {channel}  about the topic in treble backtick 
    
    ```{topic}``` .

    The audience persona is {persona} and the tone is {tone}.

    The goal of the post is to {purpose}.

    Use at most {words} words. Language is {language}.

    Generate the output as a JSON object, for example:

    "Post1": "...",
    "Post2": "...",
    "Post3": "...",

    """

    return prompt
