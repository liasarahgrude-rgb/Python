##Agora, você vai aprimorar o aplicativo anterior para torná-lo interativo, coletando e processando entradas do usuário. Você deve usar os widgets de entrada e as funções de feedback que aprendeu na segunda etapa. No arquivo boas_vindas.py, adicione uma nova seção abaixo do divisor. Use st.header() com o título "Interação com o Usuário". Crie uma caixa de texto usando st.text_input() com o rótulo "Qual o seu nome?". Armazene a entrada do usuário em uma variável. Crie um st.button() com o texto "Cumprimentar". Utilize uma estrutura if para verificar se o botão foi clicado. Se sim: a. Exiba uma mensagem de sucesso usando st.success() com o texto "Ação realizada com sucesso!". b. Utilize st.write() para exibir um cumprimento personalizado, como "Olá, [Nome do Usuário]! É um prazer ter você aqui.". c. Crie um menu de seleção de opções (dropdown) usando st.selectbox() com o rótulo "Escolha seu status:" e as opções "Aluno", "Professor", "Visitante". Exiba o valor selecionado em um texto logo abaixo do menu
import streamlit as st
st.title("Bem-vindo ao Meu Primeiro App Streamlit Divos e Divas!")
st.header("Sobre o meu app:")
st.write("Este aplicativo foi criado para demonstrar os conceitos básicos de Streamlit, como exibição de texto e a estrutura de um app")
st.header("Interação com o Usuário")
nome = st.text_input("Qual o seu nome?")## Cria uma caixa de texto para o usuário digitar seu nome e armazena a entrada na variável 'nome'
apertou = st.button("Cumprimentar")
if apertou:
  st.success("Ação realizada com sucesso!")
  st.write(f"Olá, {nome}! É um prazer ter você aqui.")
status = st.selectbox("Escolha seu status:" ,
  ["Aluno", "Professor", "Visitante"] )
st.write(status)
st.divider()


