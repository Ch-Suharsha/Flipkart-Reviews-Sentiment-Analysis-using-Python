import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import re
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

from google.colab import files
upload=files.upload()
data = pd.read_csv('flipkart_data.csv')
data.head()

# unique ratings
pd.unique(data['rating'])

sns.countplot(data=data,
			x='rating',
			order=data.rating.value_counts().index)

# rating label(final)
pos_neg = []
for i in range(len(data['rating'])):
	if data['rating'][i] >= 5:
		pos_neg.append(1)
	else:
		pos_neg.append(0)

data['label'] = pos_neg

from tqdm import tqdm


def preprocess_text(text_data):
	preprocessed_text = []

	for sentence in tqdm(text_data):
		# Removing punctuations
		sentence = re.sub(r'[^\w\s]', '', sentence)

		# Converting lowercase and removing stopwords
		preprocessed_text.append(' '.join(token.lower()
										for token in nltk.word_tokenize(sentence)
										if token.lower() not in stopwords.words('english')))

	return preprocessed_text

import nltk

def preprocess_text(text_data):
  """
  This function preprocesses the text data by converting it to lowercase, removing stopwords, and tokenizing it.

  Args:
    text_data: The text data to be preprocessed.

  Returns:
    The preprocessed text data.
  """

  # Convert the text data to lowercase.
  text_data = text_data.lower()

  # Remove stopwords from the text data.
  stopwords = nltk.corpus.stopwords.words('english')
  text_data = ' '.join([token for token in nltk.word_tokenize(text_data) if token.lower() not in stopwords])

  # Tokenize the text data.
  text_data = nltk.word_tokenize(text_data)

  return text_data

data['review'] = data['review'].astype(str)

preprocessed_review = preprocess_text(data['review'].values.astype(str))
data['review'] = preprocessed_review

data.head()

data["label"].value_counts()

cv = TfidfVectorizer(max_features=2500)
X = cv.fit_transform(data['review'] ).toarray()

X


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, data['label'],
													test_size=0.33,
													stratify=data['label'],
													random_state = 42)


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

model = DecisionTreeClassifier(random_state=0)
model.fit(X_train,y_train)

#testing the model
pred = model.predict(X_train)
print(accuracy_score(y_train,pred))

from sklearn.metrics import confusion_matrix

from sklearn import metrics
cm = confusion_matrix(y_train,pred)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm,
											display_labels = [False, True])

cm_display.plot()
plt.show()

