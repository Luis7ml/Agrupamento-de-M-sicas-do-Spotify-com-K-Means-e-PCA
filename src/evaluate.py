import pandas as pd
import matplotlib.pyplot as plt

def evaluate(kmeans, labels, X_pca, wcss):
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(wcss) + 1), wcss, marker="")
    plt.title('Método wcss')
    plt.xlabel('Numero de clusters')
    plt.ylabel('WCSS')  
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=labels,
    cmap="tab10")

    plt.title("Clusters")
    plt.xlabel("PCA 1")
    plt.ylabel("PCA 2")
    plt.show()