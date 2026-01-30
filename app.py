import streamlit as st
import pandas as pd
import joblib
import os

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

@st.cache_resource
def load_model():
    if os.path.exists('weights/modelo_avc_final.pkl'):
        return joblib.load('weights/modelo_avc_final.pkl')
    else:
        st.error("O arquivo do modelo não foi encontrado.")
        return None
    
model = load_model()

expected_columns = [
    'age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi',
    'gender_Female', 'gender_Male', 'gender_Other',
    'ever_married_No', 'ever_married_Yes',
    'work_type_Govt_job', 'work_type_Never_worked', 'work_type_Private',
    'work_type_Self-employed', 'work_type_children',
    'Residence_type_Rural', 'Residence_type_Urban',
    'smoking_status_Unknown', 'smoking_status_formerly smoked',
    'smoking_status_never smoked', 'smoking_status_smokes'
]

submit_btn = st.button("Calcular Risco de AVC", use_container_width=True)

if submit_btn and model:
    input_data = {col: 0 for col in expected_columns}

    # numeric data
    input_data['age'] = age
    input_data['hypertension'] = hypertension_map[hypertension]
    input_data['heart_disease'] = heart_disease_map[heart_disease]
    input_data['avg_glucose_level'] = avg_glucose_level
    input_data['bmi'] = bmi

    # non numeric data
    input_data[f"gender_{gender_map[gender]}"] = 1
    input_data[f"ever_married_{married_map[ever_married]}"] = 1
    input_data[f"work_type_{work_type_map[work_type]}"] = 1
    input_data[f"Residence_type_{residence_map[residence_type]}"] = 1
    input_data[f"smoking_status_{smoking_map[smoking_status]}"] = 1

    df_input = pd.DataFrame([input_data])
    df_input = df_input[expected_columns]

    try:
        prediction = model.predict(df_input)[0]
        probability = model.predict_proba(df_input)[0][1]

        st.subheader("Resultado da Análise:")
        
        if prediction == 1:
            st.error(f"⚠️ Alto risco de AVC detectado.")
            st.write(f"O modelo estima uma probabilidade de **{probability:.1%}**.")
            st.warning("Recomendação: Procure um médico para uma avaliação detalhada.")
        else:
            st.success(f"✅ Baixo risco de AVC detectado.")
            st.write(f"O modelo estima uma probabilidade de **{probability:.1%}**.")
            
    except Exception as e:
        st.error(f"Erro ao processar a previsão: {e}")