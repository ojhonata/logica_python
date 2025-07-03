import google.generativeai as genai # google.generativeai importa a parte específica do gemini IA

genai.configure(api_key="AIzaSyCyLGUZ3j_Z5kargy23bI7KENXu9m26DoI") # defina a chave da api
model= genai.GenerativeModel(model_name="gemini-2.0-flash") # defini o modelo da IA

historico = []
while True:
    usuario = input('Você: ')

    if usuario:
        historico.append({'role': 'user', 'parts': [usuario]}) # adiciona o texto do usuário na lista vazia
        response = model.generate_content(historico) # defini o modelo da IA, função que envia o prompt da lista de historico
        historico.append({'role': 'model', 'parts': [response.text]}) # adiciona a resposta da IA no histórico
        print(f'Gemini: {response.text}')
    else:
        break

'''
{'role': 'user', 'parts': [usuario]} 
role = indique quem está falando (user, model)
parts = retorna uma lista com a resposta contendo texto, imagens, etc..
'''