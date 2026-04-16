##Nesta etapa, você construirá um aplicativo de controle de estoque simples para praticar a exibição de dados tabulares e a coleta de múltiplas entradas. Crie um novo arquivo Python chamado controle_estoque.py. Utilize st.title() para o título "Controle de Estoque de Produtos". Crie um st.header() com o título "Filtros de Visualização". Utilize st.multiselect() para permitir que o usuário selecione uma ou mais categorias de produtos. Use uma lista de opções como ['Eletrônicos', 'Vestuário', 'Alimentos']. Armazene a seleção em uma variável. Abaixo do multiselect, use st.checkbox() com o rótulo "Mostrar itens com estoque baixo". Crie um st.button() com o texto "Aplicar Filtros". Crie um DataFrame do Pandas com dados de produtos, incluindo colunas como 'Produto', 'Categoria' e 'Estoque'. Certifique-se de que alguns produtos tenham estoque baixo (por exemplo, < 10 unidades). Utilize a lógica if st.button(...) para, quando o botão for clicado, exibir os dados. Dentro do if: a. Se o checkbox de "Mostrar itens com estoque baixo" estiver marcado, filtre o DataFrame para mostrar apenas os itens com estoque baixo. b. Selecione apenas as linhas do DataFrame que correspondem às categorias escolhidas no st.multiselect(). c. Exiba o DataFrame filtrado usando st.dataframe() com um subtítulo como "Itens Filtrados".
import streamlit as st  # Importa o Streamlit para criar a interface
import pandas as pd     # Importa o Pandas para manipular tabelas de dados

# Define o título principal da página
st.title("Controle de Estoque de Produtos")

# Define um cabeçalho para a seção de filtros
st.header("Filtros de Visualização")

# Cria uma caixa de seleção múltipla. 
# O que o usuário escolher será guardado na variável 'opcoes_prod' como uma LISTA.
opcoes_prod = st.multiselect(
    'Escolha os produtos que deseja: ',
    ['Eletrônicos', 'Vestuário', 'Alimentos']
)

# Cria uma caixa de marcar (Sim/Não). 
# Se estiver marcada, a variável 'mostrar' será True. Se não, será False.
mostrar = st.checkbox("Mostrar itens com estoque baixo")

# Cria um botão. O código dentro deste 'if' só roda no momento em que o botão é clicado.
if st.button("Aplicar Filtros"):
    
    # Cria um Dicionário Python com os dados simulados do estoque
    opcoes_prod1 = {
        "Produto": ["Celular", "Roupa", "Biscoito"],
        "Categoria": ["Eletrônicos", "Vestuário", "Alimentos"],
        "Estoque": [1, 2, 3] 
    }
    
    # Converte o dicionário acima em um DataFrame (uma tabela estilo Excel)
    df = pd.DataFrame(opcoes_prod1)

    # FILTRAGEM 1: Filtra a tabela para mostrar apenas as categorias que 
    # o usuário selecionou lá no multiselect ('opcoes_prod').
    df_filtrado = df[df['Categoria'].isin(opcoes_prod)]

    # FILTRAGEM 2: Se o checkbox 'mostrar' estiver marcado (True)...
    if mostrar:
        # ...ele filtra a tabela novamente para manter apenas itens com estoque menor que 10.
        df_filtrado = df_filtrado[df_filtrado['Estoque'] < 10]                                         
    
    # Exibe a tabela final (filtrada) na tela do aplicativo
    st.dataframe(df_filtrado)