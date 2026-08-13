import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate(kmeans, labels, X_pca, wcss):
    plt.figure(figsize=(8, 5))
    sns.lineplot(x=range(1, len(wcss) + 1), y=wcss)
    plt.title('Método wcss')
    plt.xlabel('Numero de clusters')
    plt.ylabel('WCSS') 
    plt.legend() 
    plt.show()
    
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x=X_pca[:, 0],
        y=X_pca[:, 1], hue=labels, palette='bright')
    plt.title("Clusters")
    plt.xlabel("PCA 1")
    plt.ylabel("PCA 2")
    plt.show()