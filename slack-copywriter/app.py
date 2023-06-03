import os
import json

import openai
from flask import Flask, redirect, render_template, request, url_for

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
    with open('reference/comm_chart.json', 'r') as fp:
        comm_chart = json.load(fp)

    if request.method == "POST":

        topic = request.form["topic"]
        tone = request.form["tone"]
        languagetype = request.form["languagetype"]
        persona = request.form["persona"]
        purpose = request.form["purpose"]
        language = request.form["language"]

        prompt = one_shot_prompt(
            words = 30,
            type = "post",
            channel = "Twitter",
            topic=topic,
            persona = persona,
            tone=tone,
            languagetype = languagetype,
            purpose = purpose,
            language = language)

        response = get_completion(prompt)
        resjson = json.loads(response)
        print(resjson)
    
        return redirect(url_for(
             "index", 
             result= response,
             personas=comm_chart["Persona"],
             tones=comm_chart["Tone"],
             languagetypes=comm_chart["LanguageType"],
             purposes=comm_chart["Purpose"],
             languages=comm_chart["Language"],
             ))
    
    elif request.method == "GET":
        
        result = request.args.get("result") # None

        return render_template(
            "index.html", 
            result=result,
            personas=comm_chart["Persona"],
            tones=comm_chart["Tone"],
            languagetypes=comm_chart["LanguageType"],
            purposes=comm_chart["Purpose"],
            languages=comm_chart["Language"],
                               )


def get_completion(prompt, model="gpt-3.5-turbo", temperature = 0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]



def one_shot_prompt(words = None, 
             type = None, 
             channel = None, 
             topic = None, 
             persona = None, 
             tone = None, 
             languagetype = None, 
             purpose = None,
             language = None):
    
    prompt = f"""

    Write three post for {channel}  about 
    
    the topic in treble backtick ```{topic}``` .

    The audiene persona is {persona} and the tone is {tone}.

    Use a {languagetype} language. The goal of the post is to {purpose}.

    Use at most {words} words.

    Language is {language}.

    Generate the output as a JSON object, for example:

    "Post1": "...",
    "Post2": "...",
    "Post3": "...",

    """
    
    return prompt


