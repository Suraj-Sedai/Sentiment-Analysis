# Sentiment Analysis Project

## 📌 Description
This project performs sentiment analysis on user comments using **TextBlob**. The data is cleaned using **NLTK** before applying sentiment classification.

## 📂 Project Structure
```
Sentiment-Analysis/
├── data/
│   ├── raw_sentiment_data.csv   # Store the dataset here
├── notebooks/
│   ├── sentiment_analysis.ipynb  # Jupyter Notebook for analysis
├── scripts/
│   ├── preprocess.py  # Text cleaning functions
│   ├── analyze.py  # Sentiment analysis function
├── requirements.txt  # List of dependencies
├── README.md  # Project documentation
├── .gitignore  # Ignore unnecessary files
```

## 🛠 Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/Suraj-Sedai/Sentiment-Analysis.git]
   ```
2. Navigate to the project folder:
   ```bash
   cd Sentiment-Analysis
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 How to Use
Run the Jupyter Notebook inside `notebooks/` to see the sentiment analysis in action.

## 📊 Example Output
| Comment | Sentiment |
|---------|----------|
| I love this product! | Positive |
| This is the worst experience ever. | Negative |

## 🎯 Features
- Data Cleaning with **NLTK**
- Sentiment Analysis using **TextBlob**
- Data Visualization with **Matplotlib & Seaborn**

---
