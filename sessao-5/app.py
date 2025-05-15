import constants
import llm
import streamlit as st

st.title('Gerador de relatório financeiro')

empresa = st.sidebar.selectbox(
    'Selecione a empresa', options=constants.EMPRESAS
)
trimestre = st.sidebar.selectbox(
    'Selecione o trimestre', options=constants.TRIMESTRES
)
ano = st.sidebar.selectbox('Selecione o ano', options=constants.ANOS)
periodo = f'{trimestre} {ano}'
idioma = st.sidebar.selectbox('Selecione o idioma', options=constants.IDIOMAS)
analise = st.sidebar.selectbox(
    'Selecione a análise', options=constants.ANALISES
)

if st.sidebar.button('Gerar relatório'):
    with st.spinner('Gerando o relatório...'):
        prompt = llm.prompt_template.format(
            empresa=empresa, periodo=periodo, idioma=idioma, analise=analise
        )

        response = llm.openai.invoke(prompt)

    st.subheader('Relatório gerado')
    st.write(response.content)
