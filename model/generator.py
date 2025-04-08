import torch
from model.text_encoder import encode_text

def generate_emoji(text):
    embedding = encode_text(text)
    if torch.argmax(embedding).item() % 3 == 0:
        return "assets/happy.png"
    elif torch.argmax(embedding).item() % 3 == 1:
        return "assets/tired.png"
    else:
        return "assets/default.png"
