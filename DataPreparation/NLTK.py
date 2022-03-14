import string
import regex as re
import nltk 
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

#split into sentences
# sentences = sent_tokenize(text)
# print(sentences[0]) 

#split into words
tokens = word_tokenize(text)

#convert to lowercase
tokens = [w.lower() for w in tokens]

#prepare regex for char filtering
re_punc = re.compile('[%s]' % re.escape(string.punctuation))

#remove punctuation from each word
stripped = [re_punc.sub('', w) for w in tokens]

#remove all remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]

#filter out stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]

print(words[:100])

