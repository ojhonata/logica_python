from google import genai

client = genai.Client(api_key="AIzaSyCyLGUZ3j_Z5kargy23bI7KENXu9m26DoI")
prompt = 'faça um resumo sem titulos e subtitulos referente a oficina de hoje "Conceitos básicos de higiene e requisitos de higiene na indústria de alimentos." O Resumo deverá ter:  Introdução, Desenvolvimento e Conclusão. Mínimo de 20 linhas.  Mínimo de 3 parágrafos.Introdução: Apresente o tema do dia em um parágrafo.  Desenvolvimento: Descreva o que aprendeu. 💡 Conclusão: Compartilhe como esse aprendizado pode ser útil na sua vida profissional ou pessoal.'

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt
)
print(response.text)