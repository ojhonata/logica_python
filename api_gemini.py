import google.generativeai as genai

genai.configure(api_key="AIzaSyCyLGUZ3j_Z5kargy23bI7KENXu9m26DoI")
model= genai.GenerativeModel(model_name="gemini-2.0-flash")

historico = []
while True:
    usuario = input('Você: ')

    if usuario:
        historico.append({'role': 'user', 'parts': [usuario]})
        response = model.generate_content(historico)
        print(f'Gemini: {response.text}')
        historico.append({'role': 'model', 'parts': [response.text]})
    else:
        break
