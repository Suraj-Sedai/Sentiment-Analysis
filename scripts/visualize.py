import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_distribution(data):
    plt.figure(figsize=(8, 6))
    sns.countplot(x='sentiment', data=data)
    plt.title('Sentiment Analysis')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()
