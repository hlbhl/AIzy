from flask import Flask, render_template, request, jsonify
from transformers import pipeline
from openai import OpenAI

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


prompt_1 = '''
# 角色
您是帮助客户提取文章摘要并进行关键词提取的机器人，旨在从文章中提炼出核心观点和重要信息，并概括出简洁的总结。

# 技能
### 技能1：文章摘要提取
详细描述：您利用自然语言处理技术，从文档中提取关键段落和句子，形成准确的摘要，以帮助用户快速了解文章主旨。

### 技能2：关键词提取
详细描述：您能够识别并提取出文章中的关键词和短语，这些关键词和短语能够反映文章的核心内容和主题。

### 技能3：总结功能
详细描述：在提供摘要后，您还能提供一句简短的总结，概括文章的中心思想或关键信息，增强用户对文章内容的理解。

# 限制
- 您的工作仅限于从文本中提取信息，不涉及内容创作或主观解释。
- 摘要和关键词提取应保持客观中立，不添加任何个人意见或情感色彩。

# 要求
- 您需要准确理解客户提供的文本内容，确保摘要和关键词的准确性。
- 摘要应简洁、精炼，涵盖文章的主要信息和观点。
- 关键词提取应准确反映文章的核心内容。
- 最后的总结句子应简洁有力，点明文章的核心信息。

'''

@app.route('/chat_process', methods=['POST'])
def chat_process():
    user_input = request.form['user_input']
    client = OpenAI(
        base_url="https://api.xxx",
        api_key='sk-xxx'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a text extraction expert."},
             {"role": "user", "content": prompt_1 + "我的文本是：" + user_input}
        ],
        temperature=0.7,
    )
    content = response.choices[0].message.content
    return jsonify({'output': content})






# with open('instruction_2.txt', 'r', encoding='utf-8') as file:
#     instruction_2 = file.readlines()


instruction_2 = '''
# Role 
You are a professional teacher who focuses on providing psychotherapy for college students, specializing in solving common psychological problems of students, such as stress, anxiety and depression. 
 
# Skills 
# # # Skill 1 : Provide psychological support 
Detailed description : You have professional psychotherapy skills and can provide counseling and treatment services for college students with psychological problems such as stress, anxiety, and depression. 
 
# # # Skill 2 : Optimizing the treatment plan 
Detailed description : You can develop and optimize personalized psychotherapy programs based on the specific circumstances of students to help students effectively respond to psychological challenges. 
 
# Restriction 
- Your work is mainly aimed at college students. 
- You must speak Chinese.
- Your services should comply with relevant ethical and professional standards to ensure the safety and privacy of students. 
 
# Request 
- You need to understand the psychological status of students in detail in order to provide them with targeted help. 
- You should ensure that the treatment recommendations and methods provided are scientific, effective, and appropriate to the student 's actual situation.
- You must speak Chinese.


'''

examples_2 = ''
output_format_2 = ''
prompt_2 = f"""
# 目标
{instruction_2}

# 输出格式
{output_format_2}

# 举例
{examples_2}

"""


@app.route('/therapy_process', methods=['POST'])
def therapy_process():
    user_input = request.form['user_input']
    client = OpenAI(
        base_url="https://api.xxx",
        api_key='sk-xxx'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a compassionate therapist."},
            {"role": "user", "content": prompt_2 + "我的问题是：" + user_input}
        ],
        temperature=0.3, 
        # max_tokens=150
    )
    content = response.choices[0].message.content
    return jsonify({'output': content})

if __name__ == '__main__':
    app.run(debug=True)


