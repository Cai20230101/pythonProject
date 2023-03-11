import time

import openai
import requests
# Your OpenAI API Key
api_key = "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"


openai.api_key = api_key

q = "用python实现：提示手动输入3个不同的3位数区间，输入结束后计算这3个区间的交集，并输出结果区间"
rsp = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "一个有10年Python开发经验的资深算法工程师"},
        {"role": "user", "content": q}
    ]
)

print(rsp)

time.sleep(5)