from flask import Flask, render_template, request, jsonify
from transformers import pipeline
from openai import OpenAI

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

from flask import Flask, request, jsonify, session
from flask_session import Session  # 需要安装 flask-session

app.config["SESSION_TYPE"] = "filesystem"  # 使用文件系统存储会话
Session(app)

@app.route('/chat_process', methods=['POST'])
def chat_process():
    user_input = request.form['user_input']
    
    # 检查用户输入是否为角色关键词，如果是则更新 session 中的角色
    if user_input in ["默认", "知心姐姐", "成熟大叔", "成功人士", "学校老师"]:
        session['current_role'] = user_input
    else:
        # 如果不是关键词，保持当前角色或设置为默认
        session['current_role'] = session.get('current_role', '默认')

    client = OpenAI(
        base_url="https://api.xiaoai.plus/v1",
        api_key='sk-v18yU6VXxR76nNYV950e7a83Fb7a4d1b9c1341E41c3aB254'
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "角色关键词：" + session['current_role'] + " 用户输入：" + user_input}
        ],
        temperature=0.7,
    )
    content = response.choices[0].message.content
    return jsonify({'output':'('+ session['current_role'] +')：'+ content + "\n（可以输入你想与你聊天的角色触发彩蛋模式：知心姐姐 成熟大叔 成功人士 学校老师）"})






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
        base_url="https://api.xiaoai.plus/v1",
        api_key='sk-v18yU6VXxR76nNYV950e7a83Fb7a4d1b9c1341E41c3aB254'
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


