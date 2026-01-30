# 🧠 NeuroPrev

### Triagem Inteligente para Acidente Vascular Cerebral (AVC)

O **NeuroPrev** é uma solução *HealthTech* que utiliza **Inteligência Artificial** para realizar a **triagem inteligente de pacientes com risco de Acidente Vascular Cerebral (AVC)**.
O projeto surgiu da necessidade de **otimizar o fluxo clínico** e **reduzir o tempo de resposta** em diagnósticos críticos, onde **cada minuto conta**.

---

## 📌 O Problema

O AVC é a **2ª maior causa de morte no mundo** e apresenta desafios relevantes no cenário atual da saúde:

* **Janela de Prevenção**
  Cerca de **90% dos casos de AVC poderiam ser evitados** com controle adequado de fatores de risco tratáveis.

* **Gargalos Clínicos**
  Escassez de especialistas disponíveis 24/7 e fluxos tradicionais de triagem lentos e pouco prioritários.

* **Impacto Global**
  Aproximadamente **25% dos adultos com mais de 25 anos** sofrerão um AVC ao longo da vida.

---

## 🚀 A Solução

O **NeuroPrev** atua como um **Sistema de Apoio à Decisão Clínica**, utilizando **Machine Learning** para identificar pacientes com maior risco de AVC e **priorizar o atendimento**.

### 🔍 Funcionalidades Principais

* **Identificação de Riscos**
  Análise de fatores como:

  * Idade
  * Hipertensão
  * Doença cardíaca
  * IMC
  * Nível médio de glicose
  * Estilo de vida e hábitos (tabagismo)

* **Triagem Inteligente**
  Priorização automática de pacientes com maior risco, auxiliando profissionais de saúde na tomada de decisão.

---

## 📊 Performance do Modelo (XGBoost)

O modelo adotado foi o **XGBoost (Extreme Gradient Boosting)**, que utiliza **árvores de decisão sequenciais**, onde cada nova árvore corrige os erros das anteriores.
Esse algoritmo é especialmente indicado para **bases de dados desbalanceadas**, como no cenário de AVC (**~95% sem AVC vs ~5% com risco**).

### 📈 Relatório de Classificação

| Classe           | Precisão | Recall (Sensibilidade) | F1-Score | Suporte |
| ---------------- | -------- | ---------------------- | -------- | ------- |
| 0 (Sem AVC)      | 0.99     | 0.62                   | 0.76     | 971     |
| 1 (Risco de AVC) | 0.11     | 0.86                   | 0.19     | 51      |

**Acurácia Geral:** **0.63**
**Total de amostras:** **1022**

### 📝 Nota Técnica

O modelo foi **otimizado para maximizar o Recall da classe positiva (0.86)**, priorizando a identificação de pacientes com risco real de AVC.
Em aplicações médicas de **triagem**, reduzir **falsos negativos** é mais importante do que maximizar a precisão, justificando a maior taxa de falsos positivos.

---

## 📦 Pesos do Modelo

Os pesos do modelo treinado estão disponíveis no diretório:

```
weights/
└── xgb_model.pkl
```

O modelo foi salvo utilizando `OPTUNA`.

📌 **Observação**
Os pesos já estão incluídos no projeto. Não é necessário retreinar o modelo para executar a inferência ou utilizar o aplicativo.

---

## ⚙️ Configurações do Modelo

* **Threshold de decisão:** 0.4
* **Tratamento de IMC ausente:** mediana (28.0)
* **Codificação:** One-Hot Encoding

---

## ▶️ Instalação do Ambiente

### Pré-requisitos

* Python 3.9+
* Pip
* Virtualenv (opcional)

###  Clone o repositório

```bash
git clone https://github.com/seu-usuario/neuroprev.git
cd neuroprev
```



###  Instale as dependências

```bash
pip install pandas scikit-learn xgboost joblib streamlit jupyter
```

---

## 📓 Execução dos Notebooks

* `analise.ipynb` → Análise exploratória dos dados (EDA)
* `treinamento.ipynb` → Treinamento e avaliação do modelo
* `inferência.ipynb` → Testes de predição com novos dados


```bash
jupyter notebook
```

---

## 🖥️ Execução do Aplicativo (Streamlit)

```bash
streamlit run app.py
```

O aplicativo ficará disponível em:

```
http://localhost:8501
```

### Funcionalidades do App

* Entrada de dados clínicos
* Cálculo da probabilidade de AVC
* Classificação automática de risco

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Machine Learning:** XGBoost
* **Bibliotecas:** Scikit-learn, Pandas, Joblib
* **Interface:** Streamlit
* **Design:** Figma

---

## 👥 Equipe

* **Alice Barbosa** — Documentação técnica, treinamento e otimização
* **Felipe Almeida** — Documentação técnica, treinamento e otimização
* **Luís Eduardo** — Desenvolvimento do Data App e treinamento dos modelos
* **Mairon Nunes** — Documentação técnica e treinamento dos modelos preditivos
* **Roni Oliveira** — Documentação técnica, treinamento e otimização

---

## ⚠️ Aviso Importante
O **NeuroPrev** é uma ferramenta de apoio à decisão clínica e **não substitui diagnóstico médico**.
Os resultados devem ser interpretados por **profissionais de saúde qualificados**.
O **NeuroPrev** é uma ferramenta de apoio à decisão clínica e **não substitui diagnóstico médico**.
Os resultados devem ser interpretados por **profissionais de saúde qualificados**.
