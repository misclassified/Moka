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
    
    You are a professional copywriter working for a digital marketing agency.

    Your task is to write **three unique social media posts** for the {channel}
    platform based on the topic provided below. The content should feel authentic,
    engaging, and aligned with the platform's style.

    Topic:
    ```{topic}```

    Audience persona: {persona}  
    Tone of voice: {tone}  
    Purpose of the posts: {purpose}  
    Maximum word count per post: {words}  
    Language: {language}  

    **Guidelines:**
    - Adapt writing style to fit the expectations and norms of the {channel} audience (e.g., punchy for Twitter, visual for Instagram, conversational for LinkedIn).
    - Avoid generic marketing buzzwords unless they are natural to the persona and purpose.
    - Each post should be distinct, not a rephrased version of the same message.
    - Incorporate relevant hashtags or emojis **only if appropriate for the channel and tone.**
    - Keep formatting minimal (no markdown, no titles, just clean text).

    Generate the output as a JSON object, for example:

    "Post1": "...",
    "Post2": "...",
    "Post3": "...",
    """
    
    return prompt
