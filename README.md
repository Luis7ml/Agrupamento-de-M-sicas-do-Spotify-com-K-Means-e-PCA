# 🎵 Spotify Songs Clustering

Projeto de Machine Learning desenvolvido para agrupar músicas do Spotify utilizando o algoritmo K-Means. O objetivo é identificar padrões entre as músicas com base em suas características de áudio, permitindo a descoberta de grupos semelhantes sem utilizar rótulos previamente definidos.

---

## 📖 Sobre o Projeto

O projeto utiliza técnicas de aprendizado não supervisionado para segmentar músicas em diferentes clusters de acordo com suas características musicais.

Além do agrupamento, foi utilizada a técnica de redução de dimensionalidade PCA para visualizar os clusters em duas dimensões.

---

## 🎯 Objetivo

Agrupar músicas com características semelhantes utilizando o algoritmo K-Means e visualizar os resultados através da redução de dimensionalidade com PCA.

---

## 📊 Dataset

O conjunto de dados contém diversas características das músicas, como:

- Danceability
- Energy
- Loudness
- Speechiness
- Acousticness
- Instrumentalness
- Liveness
- Valence
- Time
- Duration_ms
- time_signature

Essas variáveis foram utilizadas para identificar padrões entre as músicas.

---

## 🛠 Tecnologias Utilizadas

- Python
- Pandas
- Scikit-learn
- Matplotlib

---

## 📂 Estrutura do Projeto

```
spotify-songs-clustering/
│
├── data/
│   └── songs.csv
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Pipeline do Projeto

1. Carregamento dos dados
2. Pré-processamento
3. Padronização das variáveis
4. Determinação do número ideal de clusters (Método do Cotovelo)
5. Treinamento do K-Means
6. Redução de dimensionalidade com PCA
7. Visualização dos clusters

---

## 🤖 Modelo Utilizado

- K-Means Clustering

---

## 📈 Técnicas Utilizadas

- StandardScaler
- K-Means
- PCA (Principal Component Analysis)
- Método do Cotovelo (WCSS)

---

## 📊 Resultados

O algoritmo foi capaz de identificar grupos distintos de músicas com características semelhantes.

Para facilitar a interpretação dos resultados, foi utilizada a técnica PCA para reduzir o conjunto de dados para duas componentes principais (PCA 1 e PCA 2), permitindo a visualização dos clusters em um gráfico bidimensional.

Os gráficos gerados incluem:

- Método do Cotovelo
- Visualização dos Clusters

---

## 👨‍💻 Autor

**Luis Santos**

- GitHub: https://github.com/Luis7ml
- LinkedIn: https://www.linkedin.com/in/luis-santtos/
