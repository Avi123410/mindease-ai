// 💬 React Chat Interface (Key Excerpt)
function ChatInput() {
  const [message, setMessage] = useState("");
  
  const handleSend = async () => {
    const riskScore = await fetch("/api/analyze", { 
      body: JSON.stringify({ text: message }),
      headers: { "Content-Type": "application/json" }
    });
    
    if (riskScore > 0.85) {
      connectToCounselor(); // Twilio API call
    }
  };

  return (
    <AccessibleTextarea 
      onChange={(e) => setMessage(e.target.value)}
      aria-label="Mental health chat input"
    />
  );
}
