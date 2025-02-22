from textblob import TextBlob

def get_sentiment(text):
    """
    Function to classify sentiment as Positive, Neutral, or Negative
    based on TextBlob sentiment polarity score.
    """
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'
