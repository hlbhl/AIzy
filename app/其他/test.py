from openai import OpenAI 

client = OpenAI(
        base_url = "https://api.xiaoai.plus/v1",
        api_key= 'sk-v18yU6VXxR76nNYV950e7a83Fb7a4d1b9c1341E41c3aB254'
    )


# 定义提示
prompt = """
你是一个强大的语言模型，能够回答各种问题并提供有用的信息。请帮助我解决以下问题：

问题: 给我解释一下量子计算的基本原理。

要求:
1. 用简洁明了的语言。
2. 包括一个简单的例子来说明。
3. 解释为什么它比传统计算机更强大。

开始回答:
"""

# 发送请求到GPT-3.5模型
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # 或使用 "gpt-3.5-turbo" 等最新的模型名称
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "tell me a joke"}
    ],
)

# 获取并打印模型的回复
reply = response
print("模型的回答:")
print(reply)