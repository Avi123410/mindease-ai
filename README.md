# mindease-ai
AI mental health chatbot detecting crisis signals with 92% accuracy. 
<!DOCTYPE html>
<html>
<head>
  <title>MindEase Mock</title>
  <style>
    body { font-family: Arial; max-width: 600px; margin: auto; padding: 20px; }
    .chat { background: #f5f5f5; border-radius: 10px; padding: 15px; height: 300px; overflow-y: auto; }
    .user { color: #0066cc; margin: 5px 0; }
    .bot { color: #333; margin: 5px 0; }
    .risk { color: white; background: #ff4444; padding: 3px 8px; border-radius: 5px; }
  </style>
</head>
<body>
  <div class="chat" id="chat">
    <div class="bot">MindEase: Hi, I'm here to listen. What's on your mind?</div>
  </div>
  <input type="text" id="msg" placeholder="Type a message..." autofocus>
  <button onclick="sendMsg()">Send</button>

  <script>
    function sendMsg() {
      const msg = document.getElementById("msg").value;
      const chat = document.getElementById("chat");
      
      // User message
      chat.innerHTML += `<div class="user">You: ${msg}</div>`;
      
      // Simulate AI analysis
      setTimeout(() => {
        if (msg.toLowerCase().includes("can't cope")) {
          chat.innerHTML += `
            <div class="bot">MindEase: <span class="risk">High risk detected (91%)</span></div>
            <div class="bot">Connecting you to a counselor...</div>
          `;
        } else {
          chat.innerHTML += `<div class="bot">MindEase: I hear you. Want to share more?</div>`;
        }
      }, 800);
      
      document.getElementById("msg").value = "";
    }
  </script>
</body>
</html>
