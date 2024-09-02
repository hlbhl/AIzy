from flask import Flask, request, jsonify, session
from flask_session import Session  # 需要安装 flask-session

app = Flask(__name__)
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
