import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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
    to write three post for {channel}  about the topic in treble backtick. 
    Make sure the message sounds as authentic as possible.
    
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
