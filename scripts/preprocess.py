import re
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already present
nltk.download('stopwords')
stop = set(stopwords.words('english'))

def clean_text(text):
    """
    Function to clean text by:
    - Converting to lowercase
    - Removing punctuation
    - Removing numbers
    - Removing stopwords
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  
    text = re.sub(r'\d+', '', text)  
    text = ' '.join([word for word in text.split() if word not in stop])
    return text
