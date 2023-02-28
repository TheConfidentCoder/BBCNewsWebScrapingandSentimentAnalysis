# This code uses the NLTK library's pre-trained Vader sentiment analysis model to analyze the sentiment of the text file. 
# The text file is read using Python's built-in open() function, and the contents are assigned to the text variable. 
# The SentimentIntensityAnalyzer() function is used to create a sentiment analyzer object, which is used to compute the sentiment scores using the polarity_scores() method. 
# The resulting scores are then printed to the console.

# The sentiment analysis model assigns sentiment scores to the input text in four categories: negative (neg), neutral (neu), positive (pos), and compound (compound). 
# Each score represents the estimated proportion of the input text that expresses the corresponding sentiment category.
# The compound score is a normalized score that ranges from -1 (most negative) to 1 (most positive), where a score of 0 indicates a neutral sentiment. 

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Open the text file and read its contents
with open('bbcnewsheadlines.txt', 'r') as file:
    text = file.read()

# Create a sentiment analyzer object
sid = SentimentIntensityAnalyzer()

# Perform sentiment analysis on the text
scores = sid.polarity_scores(text)

# Output the sentiment scores
print('Sentiment Scores:', scores)

