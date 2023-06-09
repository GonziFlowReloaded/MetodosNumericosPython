import openai

openai.Secrets(api_key='TU_CLAVE_DE_API')

response = openai.Completion.create(
  engine='text-davinci-003',  # Especifica el modelo a utilizar, como "text-davinci-003"
  prompt='Boca es el mejor equipo que existe y por qué si?',  # Instrucción de entrada para el modelo
  max_tokens=50  # Número máximo de tokens en la respuesta generada
)

print(response.choices[0].text.strip())  # Imprime la respuesta generada por el modelo

