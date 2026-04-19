from openai import OpenAI
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
client = OpenAI(api_key=os.getenv("SILICONFLOW_API_KEY"), 
                base_url="https://api.siliconflow.cn/v1")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {
        "ok": True,
        "endpoint": "health",
        "data": {
            "api_status": "healthy"
        }
    }

@app.get("/plan")
def plan(user_input:str):
    return main('请根据下面需求在20句话内做学习计划',user_input)

@app.get("/split_task")
def split_task(user_input:str):
    return main('将下面的任务拆分成一个个小任务',user_input)
    
@app.get("/encourage")
def encourage(user_input:str):
    return main('根据同学输入内容体察同学状态，运用一些名言警句鼓励同学',user_input)

def main(requirement,user_input:str):
    user_input = user_input.strip()  # 防全是空格
    if not user_input:
        return {
            "ok": False,
            "endpoint": requirement,
            "error": "输入不能为空"
        }
    elif len(user_input) > 100:
        return {
            "ok": False,
            "endpoint": requirement,
            "error": "输入过长"
        }
    prompt = f"{requirement}: {user_input}"
    messages = build_messages(prompt)
    response = call_ai(messages)
    if response is None:
        return {
            "ok": False,
            "endpoint": requirement,
            "error": "请求失败"
        }
    return {
        "ok": True,
        "endpoint": requirement,
        "data": {
            "user_input": user_input,
            "task_type": requirement,
            "ai_answer": response.choices[0].message.content.strip()
        }
    }

def build_messages(user_content):
    messages=[
                {'role':"system",
                'content':'你是一个大学生学习助手。'},

                {'role': 'user', 
                'content': user_content}
            ]
    return messages
def call_ai(messages):
    try:   
        response = client.chat.completions.create(
            model="Qwen/Qwen3.5-4B",
            messages=messages,
            timeout=3000
        )
        return response
    except Exception as e:
        print("请求失败:",e)
        return None
