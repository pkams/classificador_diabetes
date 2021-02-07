import numpy as np
import joblib
import streamlit as st

model = joblib.load('melhor_model.sav')

st.sidebar.subheader('Criado por Patrick Souza.')
st.sidebar.markdown('[Linkedin](https://www.linkedin.com/in/souzapatrick/)', unsafe_allow_html=True)

st.title('Aplicativo para previsão de diabetes')
gestacao = st.number_input('Número de Gestações: ', 0.0, 17.0, step=1.0, value=15.0)
glicose = st.number_input('Concentração de Glicose: ', 0.0, 200.0, step=1.0, value=100.0)
pressao = st.number_input('Pressão Diastólica (mm Hg): ', 0.0, 122.0, step=1.0, value=50.0)
dobra = st.number_input('Espessura da Dobra Cutânea do Tríceps (mm): ', 0.0, 99.0, step=1.0, value=50.0)
insulina = st.number_input('Nível de Insulina: (mu U/ml)', 0.0, 846.0, step=0.25, value=800.0)
massacorporal = st.number_input('Índice de Massa Corporal: ', 0.0, 67.1, step=0.1, value=0.0)
heranca = st.number_input('Herança Genética: ', 0.078, 2.420, step=0.001, value=0.078)
idade = st.number_input('Idade (anos): ', 21.0, 81.0, step=1.0, value=21.0)

array = np.array([[gestacao, glicose, pressao, dobra, insulina, massacorporal, heranca, idade]])

if st.button('Enviar'):
    st.header('Previsão para os dados inseridos:')
    if model.predict(array) == [1]:
        st.text('Diabético.')
    else:
        st.text('Não diabético.')


