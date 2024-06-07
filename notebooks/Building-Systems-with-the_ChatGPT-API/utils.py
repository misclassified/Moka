
from openai import OpenAI

client = OpenAI()

def get_completion(prompt, 
                   model="gpt-3.5-turbo",
                   temperature=0,
                   max_tokens=500,
                   verbose = False):
    
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model=model,
    temperature=temperature,
    max_tokens=max_tokens
)
    
    response = chat_completion.choices[0].message.content

    if verbose:
        token_usage = chat_completion.usage.total_tokens
        print(f"A total of {token_usage} tokens was used")

    return response


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500, verbose = False):
    
    chat_completion = client.chat.completions.create(
    messages=messages,
    model=model,
    temperature=temperature,
    max_tokens=max_tokens
)
    
    response = chat_completion.choices[0].message.content

    if verbose:
        token_usage = chat_completion.usage.total_tokens
        print(f"A total of {token_usage} tokens was used")

    return response