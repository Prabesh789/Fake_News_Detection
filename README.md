# Text-Based Fake News Classification Using NLP and Supervised Learning

This project presents a machine learning-based system that detects fake news using text-based features and Natural Language Processing (NLP) techniques. It compares the performance of various classical supervised learning models on a labeled dataset of real and fake news articles.

---

## Table of Contents
- [Overview](#overview)
- [Project Architecture](#project-architecture)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Models Compared](#models-compared)
- [Results](#results)
- [How to Run](#how-to-run)
- [Dataset](#dataset)
- [Contributors](#contributors)
- [License](#license)

---

## Overview

The widespread dissemination of fake news has prompted the need for intelligent automated detection systems. This project implements six traditional machine learning models trained on preprocessed news data to identify fake versus real articles. Key NLP steps like stopword removal, lemmatization, and TF-IDF vectorization are used in the pipeline.

---

## Project Architecture

```plaintext
Load CSV Files → Merge & Label Data → Preprocessing (Lowercase, Remove Punctuation, Stopwords, Lemmatize)
→ TF-IDF Vectorization → Train-Test Split → Model Training → Evaluation → Results Visualization
```

---

## Technologies Used

- **Python 3.11**
- **Jupyter Notebook**
- **Scikit-learn**
- **Pandas, Numpy**
- **Matplotlib, Seaborn**
- **NLTK (for NLP tasks)**

---

## How It Works

1. Load and merge datasets (`True.csv` & `Fake.csv`)
2. Apply preprocessing (cleaning, stopword removal, lemmatization)
3. Convert text data into numerical features using TF-IDF
4. Train the following ML models:
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - Support Vector Machine (SVM)
   - K-Nearest Neighbors (KNN)
   - Naïve Bayes
5. Evaluate using:
   - Accuracy, Precision, Recall, F1-Score, ROC-AUC
6. Visualize results with ROC curves and confusion matrices

---

## Models Compared

| Model              | Accuracy | F1-Score | ROC-AUC | Training Time |
|--------------------|----------|----------|---------|----------------|
| Logistic Regression| 0.99     | 0.99     | 1.00    | 0.6s           |
| Decision Tree      | 1.00     | 1.00     | 1.00    | 37.6s          |
| Random Forest      | 0.99     | 0.99     | 1.00    | 118.4s         |
| SVM                | 0.99     | 0.99     | 1.00    | 1712.6s        |
| KNN                | 0.62     | 0.54     | 0.77    | 27.9s          |
| Naïve Bayes        | 0.94     | 0.94     | 0.98    | 0.0s           |

---

## How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/Prabesh789/Fake_News_Detection.git
   cd fake-news-classification
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the notebook:
   ```bash
   jupyter notebook FakeNewsDetection.ipynb
   ```

---

## Dataset

- **Source:** Kaggle
- **Files Used:**
  - `True.csv` – Real news
  - `Fake.csv` – Fake news  
- Preprocessing includes lowercase conversion, stopword removal, lemmatization, and punctuation removal.

---

## Contributors

- **Prabesh Rai** – [raiprabesh775@gmail.com](mailto:raiprabesh775@gmail.com)  
- **Amisha Shrestha** – [Amisha-777](https://github.com/Amisha-777)  
- **Pramila Poudel** – [pramilapoudel023](https://github.com/pramilapoudel023)


---

## License

This project is for academic use only.

---

## Acknowledgments

- Instructor: **Dr. Debashish Roy**, Lambton College  
- Course: **BAM-3034 – Sentiment Analysis and Text Mining**