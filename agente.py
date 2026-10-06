from groq import Groq 
import streamlit as st 



st.title ('AGENTE PROFESSORA ANA ❤️')

client = Groq(api_key = )

print('--------------------')
print()

pergunta = input('Digite sua pergunta...')
print
print('-----------------------------')
resposta = client.chat.completions.create(

model =  'openai/gpt-oss-120b',
messages=[ 

    {
    
        "role": "system",
        "content": "você é um professor educado e  simpatico"
        "",
    },
    
    {
        "role":"user", 
        "content": pergunta    
    },
],
temperature= 0.2
) 

print(resposta.choices[0].message.content)

st.write(resposta.choices[0].message.content)
''