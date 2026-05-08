from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# 🔹 (مكان الذكاء الاصطناعي الحقيقي لاحقًا)
def fake_ai_response(text):
    return f"🤖 AI Cris رد: {text}"

@app.route("/")
def home():
    return render_template("index.html")

# 🔍 كشف الصور (نسخة تجريبية)
@app.route("/detect", methods=["POST"])
def detect():
    return jsonify({
        "result": "🧠 الصورة تبدو مولدة بالذكاء الاصطناعي (نسخة تجريبية)"
    })

# 💻 توليد أكواد
@app.route("/code", methods=["POST"])
def code():
    data = request.json
    lang = data["language"]
    features = data["features"]

    code = f"""
// AI Cris Code Generator
// Language: {lang}
// Features: {features}

console.log("AI Cris generated this code");
"""
    return jsonify({"code": code})

# 💬 شات AI
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data["question"]

    return jsonify({
        "answer": fake_ai_response(question)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
