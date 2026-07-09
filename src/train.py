from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


def train_model(X_scaled):
    wcss = []
    for i in range(1, 10):
        kmeans = KMeans(n_clusters=i, random_state=0)
        kmeans.fit(X_scaled)
        wcss.append(kmeans.inertia_)


    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    kmeans = KMeans(n_clusters=3, random_state=0)
    labels = kmeans.fit_predict(X_pca)


    return kmeans, labels, X_pca, wcss