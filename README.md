#  NeuroPrev

### Triagem Inteligente para Acidente Vascular Cerebral (AVC)

O **NeuroPrev** é uma solução *HealthTech* que utiliza **Inteligência Artificial** para realizar a **triagem inteligente de pacientes com risco de Acidente Vascular Cerebral (AVC)**.
O projeto surgiu da necessidade de **otimizar o fluxo clínico** e **reduzir o tempo de resposta** em diagnósticos críticos, onde **cada minuto conta**.

---

##  O Problema

O AVC é a **2ª maior causa de morte no mundo** e apresenta desafios relevantes no cenário atual da saúde:

* **Janela de Prevenção**
  Cerca de **90% dos casos de AVC poderiam ser evitados** com controle adequado de fatores de risco tratáveis.

* **Gargalos Clínicos**
  Escassez de especialistas disponíveis 24/7 e fluxos tradicionais de triagem lentos e pouco prioritários.

* **Impacto Global**
  Aproximadamente **25% dos adultos com mais de 25 anos** sofrerão um AVC ao longo da vida.

---

##  A Solução

O **NeuroPrev** atua como um **Sistema de Apoio à Decisão Clínica**, utilizando **Machine Learning** para identificar pacientes com maior risco de AVC e **priorizar o atendimento**.

###  Funcionalidades Principais

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

##  Performance do Modelo

###  Relatório de Classificação (XGBoost + Optuna)

| Classe | Precisão | Recall | F1-Score | Suporte |
|------|---------|--------|----------|---------|
| 0 (Sem AVC) | 0.99 | 0.53 | 0.69 | 972 |
| 1 (Risco de AVC) | 0.09 | 0.94 | 0.17 | 50 |

- **Acurácia Geral:** 0.55  
- **Total de Amostras:** 1022  

###  Nota Técnica

O modelo otimizado com **Optuna** prioriza a **sensibilidade da classe de risco**, atingindo **Recall = 0.94** para pacientes com risco de AVC.  
Essa configuração reduz significativamente **falsos negativos**, característica essencial em sistemas de **triagem médica**, mesmo com impacto na precisão global.


---

##  Pesos do Modelo

Os pesos do modelo treinado estão disponíveis no diretório:

```
weights/
└── xgb_model.pkl
```

O modelo foi salvo com os pesos do hiperparametros do  `OPTUNA`.

* **Threshold de decisão:** 0.4
* **Tratamento de IMC ausente:** mediana (28.0)
* **Codificação:** One-Hot Encoding

estão disponíveis no diretório:

weights/
└── xgb_artefatos.jason


 **Observação**
Os pesos já estão incluídos no projeto. Não é necessário retreinar o modelo para executar a inferência ou utilizar o aplicativo.



## Execução dos Notebooks

O projeto já possui o **modelo treinado**, sendo necessário **apenas executar a inferência**.

### Notebooks Disponíveis

- `analise.ipynb` → Análise exploratória dos dados (EDA) *(referencial)*  
- `treinamento.ipynb` → Treinamento e avaliação do modelo *(documental)*  
- `inferência.ipynb` → **Inferência com novos dados (uso obrigatório)**  

 **Importante:**  
Para utilizar o NeuroPrev **não é necessário rodar os notebooks de análise ou treinamento**.  
O uso prático do sistema requer **somente o notebook `inferência.ipynb`**.

##  Execução do Aplicativo (Streamlit)

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

##  Tecnologias Utilizadas

* **Linguagem:** Python
* **Machine Learning:** XGBoost
* **Bibliotecas:** Scikit-learn, Pandas, Joblib
* **Interface:** Streamlit
* **Design:** Figma

---

##  Equipe

* **Alice Barbosa** — Documentação técnica, treinamento e otimização
* **Felipe Almeida** — Documentação técnica, treinamento e otimização
* **Luís Eduardo** — Desenvolvimento do Data App e treinamento dos modelos
* **Mairon Nunes** — ReadMe
* **Roni Oliveira** — Documentação técnica, treinamento e otimização

---

##  Aviso Importante
O **NeuroPrev** é uma ferramenta de apoio à decisão clínica e **não substitui diagnóstico médico**.
Os resultados devem ser interpretados por **profissionais de saúde qualificados**.
O **NeuroPrev** é uma ferramenta de apoio à decisão clínica e **não substitui diagnóstico médico**.
Os resultados devem ser interpretados por **profissionais de saúde qualificados**.
