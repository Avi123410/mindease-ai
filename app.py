# 🔥 Flask API Endpoint (Backend)
@app.route('/api/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    risk_score = model.predict(data['text'])  # Calls our PyTorch model
    
    if risk_score > 0.85:
        counselor = Firebase.get_available_counselor()
        Twilio.send_sms(counselor.phone, f"High-risk user needs help: {data['text']}")
    
    return jsonify({"risk": float(risk_score)})
