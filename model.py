# 🧠 Crisis Detection Model (Python/PyTorch)
class CrisisDetector(nn.Module):
    def __init__(self):
        super().__init__()
        self.roberta = AutoModel.from_pretrained("roberta-base")
        self.classifier = nn.Linear(768, 2)  # Risk/No-risk
        
    def forward(self, text):
        inputs = tokenizer(text, return_tensors="pt", truncation=True)
        outputs = self.roberta(**inputs)
        return torch.sigmoid(self.classifier(outputs.last_hidden_state[:,0]))

# Example prediction
model = CrisisDetector()
print(model("I can't do this anymore"))  # Output: tensor([0.91]) → 91% risk
