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


def chatbot_while(input1):
    print("chatbot_while에 들어온 값은 ",input1)
    openai.api_key = "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"
    messages=[{
        "role":"system",
        "content": """당신은 부산을 대표하는 부산 관광 가이드, 20대의 상큼한 말투와 자신감 있는 태도로 대답해줘."""
    }]
    print("input1의 길이는 >>>>> [",len(input1),"]")
    for i in input1:
        messages.append(i)
    print("chatbot.py의 messages는 ",messages)
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    assistant_content = completion.choices[0].message["content"].strip()
    #print("completion는 >>>",completion)
    assistant_content = re.sub(r'\.', '.\n', assistant_content)
    assistant_content = re.sub(r'\?', '?\n', assistant_content)
    assistant_content = re.sub(r'!', '!\n', assistant_content)

    return assistant_content
    #print(messages)
    #print(f"GPT: {assistant_content}")
    #if user_content=='q':
    #   break
