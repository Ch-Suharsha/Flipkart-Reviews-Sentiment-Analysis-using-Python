# Flipkart-Reviews-Sentiment-Analysis-using-Python

**Project Overview:**

**Objective:**
The project aims to perform sentiment analysis on user reviews from Flipkart to predict whether a given review is positive or negative. The analysis is conducted using machine learning techniques, including text preprocessing, feature extraction, and a Decision Tree classifier. The project leverages Natural Language Processing (NLP) tools to extract meaningful insights from user-generated reviews and ratings.

**Key Steps in the Project:**

1. **Data Collection:**
   - Loading the dataset containing user reviews and ratings from Flipkart.

2. **Data Exploration:**
   - Exploring unique ratings and visualizing the distribution of ratings using a count plot.

3. **Labeling Ratings:**
   - Creating a binary label indicating whether a review is positive (1) or negative (0) based on the rating.

4. **Text Preprocessing:**
   - Removing punctuations, converting text to lowercase, and removing stopwords to clean the review text.
   - Using the NLTK library for text processing.

5. **Feature Extraction:**
   - Using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to convert text data into numerical features.
   - Limiting the features to 2500 for efficiency.

6. **Train-Test Split:**
   - Splitting the dataset into training and testing sets for model evaluation.

7. **Decision Tree Classification:**
   - Implementing a Decision Tree classifier for sentiment analysis.
   - Training the model on the training set.

8. **Model Evaluation:**
   - Testing the model on the training set and calculating accuracy.
   - Visualizing the confusion matrix to assess model performance.

**Outcome:**
The project provides a predictive model for sentiment analysis on Flipkart reviews. By analyzing the textual content of reviews and their corresponding ratings, the model classifies reviews into positive or negative sentiments. The Decision Tree classifier demonstrates the effectiveness of machine learning in automated sentiment analysis.

**Conclusion:**
Sentiment analysis on e-commerce platforms, such as Flipkart, is crucial for businesses to understand customer sentiments and improve product quality and services. This project demonstrates the application of machine learning techniques to extract valuable insights from user-generated content. The accuracy of the model on the training set and the confusion matrix visualization offer a comprehensive view of the model's performance. Further enhancements may involve exploring more sophisticated models and increasing the size of the dataset for improved generalization.

