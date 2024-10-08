import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import tiktoken



model_to_use="gpt-4o-mini"

if load_dotenv('.env'):
    #For running in local via "streamlit run main.py" from cmd prompt
    API_KEY = os.getenv('OPENAI_API_KEY')
else:
    try:
        #For streamlit app at https://course-query.streamlit.app
        #This is because OPENAI_API_KEY is keep as a secret when deploying streamlit app
        API_KEY = st.secrets['OPENAI_API_KEY']
    except:
        #For docker running in local machine and CStack.cloud https://course-query.app.cstack.cloud
        #This is because OPENAI_API_KEY is keep as a env variable when running the container from a docker image
        API_KEY = os.getenv('OPENAI_API_KEY')

# Pass the API Key to the OpenAI Client
client = OpenAI(api_key=API_KEY)

def get_embedding(input, model='text-embedding-3-small'):
    response = client.embeddings.create(
        input=input,
        model=model
    )
    return [x.embedding for x in response.data]


# This is the "Updated" helper function for calling LLM
def get_completion(prompt, model=model_to_use, temperature=0, top_p=1.0, max_tokens=1024, n=1, json_output=False):
    if json_output == True:
      output_json_structure = {"type": "json_object"}
    else:
      output_json_structure = None

    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create( #originally was openai.chat.completions
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=1,
        response_format=output_json_structure,
    )
    return response.choices[0].message.content


# Note that this function directly take in "messages" as the parameter.
def get_completion_by_messages(messages, model=model_to_use, temperature=0, top_p=1.0, max_tokens=1024, n=1):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=1
    )
    return response.choices[0].message.content


# This function is for calculating the tokens given the "message"
# ⚠️ This is simplified implementation that is good enough for a rough estimation
def count_tokens(text):
    encoding = tiktoken.encoding_for_model(model_to_use)
    return len(encoding.encode(text))


def count_tokens_from_message(messages):
    encoding = tiktoken.encoding_for_model(model_to_use)
    value = ' '.join([x.get('content') for x in messages])
    return len(encoding.encode(value))
