# NeuroPrev

- Eixo A: Saúde e Bem-Estar
### Triagem Inteligente para Acidente Vascular Cerebral (AVC)

O **NeuroPrev** é uma solução *HealthTech* que utiliza **Inteligência Artificial** para realizar a **triagem inteligente de pacientes com risco de Acidente Vascular Cerebral (AVC)**.  
O projeto surgiu da necessidade de **otimizar o fluxo clínico** e **reduzir o tempo de resposta** em diagnósticos críticos, onde **cada minuto conta**.

---

## 📌 O Problema

O AVC é a **2ª maior causa de morte no mundo** anualmente e apresenta desafios significativos no cenário atual da saúde:

- **Janela de Prevenção:**  
  Aproximadamente **90% dos casos de AVC poderiam ser evitados** com o controle de fatores de risco comportamentais e tratáveis.

- **Gargalos Clínicos:**  
  Existe uma **escassez de especialistas disponíveis 24/7**, e os fluxos tradicionais de triagem costumam ser **lentos e pouco prioritários**.

- **Impacto Global:**  
  Cerca de **25% dos adultos com mais de 25 anos** terão um AVC ao longo da vida.

---

## 🚀 A Solução

O **NeuroPrev** atua como um **Sistema de Apoio à Decisão Clínica**, utilizando **Machine Learning** para identificar e priorizar pacientes com maior risco de AVC.

### 🔍 Funcionalidades Principais

- **Identificação de Riscos:**  
  Mapeamento de fatores como:
  - Diabetes  
  - Hipertensão  
  - Obesidade  
  - Estilo de vida  
  - Dados clínicos relevantes

- **Triagem Inteligente:**  
  Priorização automática de casos mais graves na fila de atendimento, auxiliando profissionais de saúde na tomada de decisão.

---

## 📊 Performance do Modelo

O modelo adotado foi o **Random Forest**, escolhido por sua **robustez no tratamento de dados clínicos** e boa capacidade de generalização.

### 📈 Relatório de Classificação

| Classe | Precisão | Recall (Sensibilidade) | F1-Score | Suporte |
|------|---------|------------------------|---------|---------|
| 0 (Saudável) | 0.99 | 0.65 | 0.79 | 971 |
| 1 (Risco de AVC) | 0.12 | 0.88 | 0.21 | 51 |

**Acurácia Geral:** **0.66**  
**Total de amostras:** **1022**

### 📝 Nota Técnica

O modelo foi **intencionalmente otimizado para maximizar o Recall (0.88)** na classe de risco (1).  
Em aplicações médicas de **triagem**, é fundamental **reduzir falsos negativos**, garantindo que **88% dos pacientes com risco real de AVC** sejam identificados e encaminhados para avaliação imediata.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python  
- **Machine Learning:** Random Forest (Scikit-learn)  
- **Interface de Usuário:**  
  - Figma (Design)  
  - Data App (Desenvolvimento)

---

## 👥 Equipe

- **Alice Barbosa**  
  Documentação técnica, treinamento e otimização do modelo.

- **Felipe Almeida**  
  Documentação técnica, treinamento e otimização do modelo.

- **Luís Eduardo**  
  Desenvolvimento do Data App e treinamento dos modelos.

- **Mairon Nunes**  
  Documentação técnica e treinamento dos modelos preditivos.

- **Roni Oliveira**  
  Documentação técnica, treinamento e otimização do modelo.

---

## 📌 Observações Finais

O **NeuroPrev** não substitui o diagnóstico médico, mas atua como uma **ferramenta de apoio**, auxiliando profissionais de saúde na **priorização de atendimentos** e na **redução do tempo de resposta** em cenários críticos.


- [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
