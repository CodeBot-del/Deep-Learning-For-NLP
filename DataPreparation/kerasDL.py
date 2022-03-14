from keras.preprocessing.text import text_to_word_sequence
from keras.preprocessing.text import one_hot
from keras.preprocessing.text import hashing_trick
# define the document
text = 'The quick brown fox jumped over the lazy dog.'
# estimate the size of the vocabulary
words = set(text_to_word_sequence(text))
vocab_size = len(words)
print(vocab_size)

# integer encode the document
result = one_hot(text, round(vocab_size*1.3)) #the vocab size is increased to avoid collisions during encoding
# print(result)


#Using the hash trick function 
result = hashing_trick(text, round(vocab_size*1.3), hash_function= 'md5' ) #specify the text to encode, vocabulary size (increase a little bit) and the hashing function
print(result)

