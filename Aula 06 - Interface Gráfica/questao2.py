import streamlit as st
import random## Importa a biblioteca random para gerar números aleatórios

# Verificamos se 'numero_secreto' já está na memória
if 'numero_secreto' not in st.session_state:##st.session_state guarda por curto período de tempo variáveis que queremos manter mesmo depois de o usuário interagir com o app
    # Se não estiver, sorteamos um e guardamos no "dicionário" de estado
    numero = random.randint(0, 100)## Gera um número aleatório entre 0 e 100 e armazena na variável
    tentativas = 5## Inicializa o número de tentativas
    ganhar = False## Inicializa o status de vitória
with st.expander("Clique para ver as regras do jogo"):
    st.markdown('''
    ### 🎮 Regras do Jogo
    1. O computador escolheu um número entre **0 e 100**.
    2. Você tem **5 tentativas** para adivinhar.
    3. A cada palpite, eu vou te dizer se o número secreto é **maior** ou **menor**.
    4. Se a distância for grande (mais de 15), eu te darei um aviso especial!
    ''', unsafe_allow_html=True)