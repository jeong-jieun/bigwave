from konlpy.tag import Okt
import re
import pandas as pd
from io import StringIO
import openai
from konlpy.tag import Okt

def chatbot_11(input1):
    openai.api_key = "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"
    okt = Okt()
    gpt_prompt=[{
        "role":"system",
        "content": "당신은 친절한 챗봇, 입력해줘"
    }]
    
    gpt_prompt.append({
        "role":"user",
        "content":input1
    })
    
    gpt_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=gpt_prompt)

    assistant_content = gpt_response["choices"][0]["message"]["content"]
    return(assistant_content)


def chatbot_one(input1):
    openai.api_key = "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"

    gpt_prompt=[{
        "role":"system",
        "content": "당신은 친절한 챗봇, 입력해줘"
    }]
    
    gpt_prompt.append({
        "role":"user",
        "content":input1
    })
    
    gpt_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=gpt_prompt)

    return gpt_response["choices"][0]["message"]["content"]


def chatbot_while(messages):
    openai.api_key = "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"
    print("1")
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    print("2")
    assistant_content = completion.choices[0].message["content"].strip()
    print(assistant_content)
    return assistant_content
    #print(messages)
    #print(f"GPT: {assistant_content}")
    #if user_content=='q':
    #   break
