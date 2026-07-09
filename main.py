from src.data_loader import load_data
from src.preprocessing import preprocess
from src.train import train_model
from src.evaluate import evaluate

def main():
    df = load_data('data/songs.csv')

    X_scaled = preprocess(df)

    kmeans, labels, X_pca, wcss = train_model(X_scaled)

    evaluate(kmeans, labels, X_pca, wcss)




if __name__ == "__main__":
    main()