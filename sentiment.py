import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


nltk.download([
    
    "stopwords",
    "state_union",
    "twitter_samples",
    "movie_reviews",
    "averaged_perceptron_tagger",
    "vader_lexicon",
    "punkt",
    ])

stopwords = nltk.corpus.stopwords.words("english")

#takes the string and lowercases it, tokenizes it, removes non-alphabet characters and stopwords
def filterString(str):
    str = str.lower()
    words = nltk.word_tokenize(str)
    words = [w for w in words if w.isalpha()]
    words_list = [w for w in words if w not in stopwords]
    filtered_str = ""
    for word in words_list:
        filtered_str = filtered_str + word + " "

    return(filtered_str)

#creates a frequency distribution of the words
def freqDist(str):
    str = str.lower()
    words = nltk.word_tokenize(str)
    words = [w for w in words if w.isalpha()]
    words_list = [w for w in words if w not in stopwords]
    fd = nltk.FreqDist(words_list)
    list = fd.most_common(3)
    print(list)
    return(f"The most common words on this website are '{list[0][0]}' ({list[0][1]} occurrences), '{list[1][0]}' ({list[1][1]} occurrences), and '{list[2][0]}' ({list[2][1]} occurrences)")
    
#performs sentiment analysis- whether it's positive, negative, neutral
def sentimentAnalyzer(str):
    sia = SentimentIntensityAnalyzer()
    dict = sia.polarity_scores(filterString(str))
    return dict
   
    