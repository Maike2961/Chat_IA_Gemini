import google.generativeai as genai
from senha import API_KEY

genai.configure(api_key=API_KEY)

for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(model.name)


model = genai.GenerativeModel("gemini-1.5-pro-latest")

question = model.generate_content("Quem criou os modelos de IA Gemini ? ")
print(question.text)

chat = model.start_chat(history=[])

prompt = input("Digite o que deseja: ")

while prompt != "sair":
    awnser = chat.send_message(prompt)
    print(awnser.text)
    prompt = input("Digite 'Sair' se Deseja Sair: ").lower()


