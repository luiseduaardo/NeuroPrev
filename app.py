import streamlit as st

st.set_page_config(page_title="NeuroPrev", page_icon="🧠")

st.title("🧠 NeuroPrev: triagem inteligente para Acidente Vascular Cerebral")
st.markdown("Insira os dados clínicos do paciente para calcular a probabilidade de AVC.")

# map parameters to portuguese
gender_map = {"Masculino": "Male", "Feminino": "Female", "Outro": "Other"}
hypertension_map = {"Não": 0, "Sim": 1}
heart_disease_map = {"Não": 0, "Sim": 1}
married_map = {"Sim": "Yes", "Não": "No"}
work_type_map = {
    "Setor Privado": "Private",
    "Autônomo": "Self-employed",
    "Serviço Público": "Govt_job",
    "Criança": "children",
    "Nunca Trabalhou": "Never_worked"
}
residence_map = {"Urbano": "Urban", "Rural": "Rural"}
smoking_map = {
    "Fumava Anteriormente": "formerly smoked",
    "Nunca Fumou": "never smoked",
    "Fuma Atualmente": "smokes",
    "Desconhecido": "Unknown"
}

# inputs
st.subheader("Dados Clínicos")

gender = st.selectbox("Gênero", list(gender_map.keys()))

age = st.number_input("Idade (anos)", min_value=0.0, max_value=120.0, value=50.0, step=1.0)

# bmi calculator if the person doesn't know how to calculate
usar_calculadora = False
usar_calculadora = st.checkbox("Não sei meu IMC (Calcular agora)")

if usar_calculadora:
    peso = st.number_input("Peso (kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.1)
    altura = st.number_input("Altura (m)", min_value=0.5, max_value=2.5, value=1.70)
    
    bmi_calculado = peso / (altura ** 2)
    bmi = bmi_calculado
    
    st.info(f"Seu IMC calculado é: **{bmi:.2f}**")
else:
    bmi = st.number_input("IMC", min_value=10.0, max_value=100.0, value=28.0)

hypertension = st.selectbox("Hipertensão", list(hypertension_map.keys()))

heart_disease = st.selectbox("Doença Cardíaca", list(heart_disease_map.keys()))

avg_glucose_level = st.number_input("Nível Médio de Glicose (mg/dL)", min_value=50.0, max_value=300.0, value=100.0)

ever_married = st.selectbox("Já foi casado(a)?", list(married_map.keys()))

work_type = st.selectbox("Tipo de Trabalho", list(work_type_map.keys()))

residence_type = st.selectbox("Tipo de Residência", list(residence_map.keys()))

smoking_status = st.selectbox("Tabagismo", list(smoking_map.keys()))

# calculate button
st.divider()
submit_btn = st.button("Calcular Risco de AVC", use_container_width=True)