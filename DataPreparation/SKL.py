from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer

#List of text documents
text = ["The quick brown fox jumped over the lazy dog."]

#create transform 
vectorizer = CountVectorizer()

#tokenize and build vocab
vectorizer.fit(text)

#summarize
# print(vectorizer.vocabulary_)

#encode document
vector = vectorizer.transform(text)

#summarize encoded vector
# print(vector.shape)
# print(type(vector))  
# print(vector.toarray())


#USING TFIDFVECTORIZER
text = ["The quick brown fox jumped over the lazy dog.",
"The dog.",
"The fox"]
# create the transform
vectorizer = TfidfVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
# print(vectorizer.vocabulary_)
# print(vectorizer.idf_)
# encode document
vector = vectorizer.transform([text[0]])
# summarize encoded vector
# print(vector.shape)
# print(vector.toarray())

#USING HASHVECTORIZER
# list of text documents
text = ["The quick brown fox jumped over the lazy dog."]
# create the transform
vectorizer = HashingVectorizer(n_features=20)  #vector size of 20
# encode document
vector = vectorizer.transform(text)
# summarize encoded vector
print(vector.shape)
print(vector.toarray())
