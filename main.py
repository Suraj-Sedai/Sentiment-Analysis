from scripts.load_data import load_data
from scripts.preprocess import preprocess_data
from scripts.analyze_sentiment import analyze_sentiment
from scripts.visualize import plot_sentiment_distribution

def main():
    data = load_data('data/raw_sentiment_data.csv')
    data = preprocess_data(data)
    data = analyze_sentiment(data)

    print(data[['Comment', 'sentiment']].head(10))
    print(data['sentiment'].value_counts())

    plot_sentiment_distribution(data)

if __name__ == '__main__':
    main()
