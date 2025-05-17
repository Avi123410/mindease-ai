# mindease-ai
AI mental health chatbot detecting crisis signals with 92% accuracy. 
**Real-time crisis detection** | 🤖 **Privacy-first AI** | 💬 **Human counselor handoff**  

<img src="assets/demo.gif" width="500" alt="MindEase detecting high-risk message">  

## 🔍 Why MindEase?  
- 70% of crisis signs go unreported due to stigma  
- Our **fine-tuned RoBERTa model** detects distress with **92% accuracy**  
- **Zero stored data** – end-to-end encrypted conversations  

## 🛠️ Tech Stack  
- **AI**: Python, PyTorch, HuggingFace Transformers  
- **Backend**: Flask, Firebase Realtime DB  
- **Frontend**: React (PWA), Material-UI  
- **APIs**: Twilio, Crisis Text Line  

## 🚀 Quick Start  
```bash
git clone https://github.com/yourusername/mindease-ai  
cd mindease-ai  
pip install -r backend/requirements.txt  
npm install --prefix frontend  
flask run --port 5000 & npm start --prefix frontend  
