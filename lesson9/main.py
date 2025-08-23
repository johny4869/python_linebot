from flask import Flask, jsonify,render_template_string, request
from google import genai
from dotenv import load_dotenv # type: ignore #處理環境變數
import os

load_dotenv() #載入env
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
print(os.environ.get("GEMINI_API_KEY"))
app = Flask(__name__)

@app.route("/")
def index():
    html = '''
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>Gemini 小助手 Chatbot</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f5f5f5; }
            .container { max-width: 900px; margin: 40px auto; background: #fff; padding: 40px; border-radius: 10px; box-shadow: 0 2px 8px #ccc; }
            h1 { text-align: center; }
            #result { min-height: 120px; background: #f0f0f0; margin-top: 20px; padding: 18px; border-radius: 5px; }
            .btn { padding: 12px 28px; margin: 6px; border: none; border-radius: 5px; cursor: pointer; font-size: 18px; }
            .btn-start { background: #4CAF50; color: #fff; }
            .btn-clear { background: #f44336; color: #fff; }
            #question { width: 100%; padding: 12px; border-radius: 5px; border: 1px solid #ccc; font-size: 16px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Gemini 小助手 Chatbot</h1>
            <input type="text" id="question" placeholder="請輸入您的問題..." />
            <div>
                <button class="btn btn-start" onclick="startChat()">開始</button>
                <button class="btn btn-clear" onclick="clearAll()">清除</button>
            </div>
            <div id="result"></div>
        </div>
        <script>
            function startChat() {
                const q = document.getElementById('question').value.trim();
                if (!q) { alert('請輸入問題'); return; }
                document.getElementById('result').innerHTML = '請稍候...';
                fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ question: q })
                })
                .then(res => res.json())
                .then(data => {
                    document.getElementById('result').innerHTML = data.html || data.text || '無回應';
                })
                .catch(() => {
                    document.getElementById('result').innerHTML = '發生錯誤，請稍後再試';
                });
            }
            function clearAll() {
                document.getElementById('question').value = '';
                document.getElementById('result').innerHTML = '';
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "").strip()
    if not question:
        return jsonify({"error": "請輸入您的問題。"}), 400
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{question},回應請輸出成為html格式,請記得您的名字是`致理小助手`"
        )
        html_format = response.text.replace("、、、html", "").replace("、、、", "")
        return jsonify({"text": html_format})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    # 在這裡處理問題並生成回應
    response = generate_response(question)
    return jsonify({"text": response})

def generate_response(question):
    # 這裡可以根據問題生成回應，目前回傳固定文字
    if not question:
        return "請輸入您的問題。"
    return f"您問的是：{question}（這是範例回應）"
