# chatbot.py
from transformers import pipeline

# Carregar modelo de NLP pré-treinado
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

def chat():
    print("Chatbot: Olá! Como posso ajudar você hoje?")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "adeus"]:
            print("Chatbot: Até logo!")
            break
        response = chatbot(user_input)
        print(f"Chatbot: {response['generated_text']}")

if __name__ == "__main__":
    chat()
