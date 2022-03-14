import regex as re
import string

#load text
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

#split into words by whitespace
words = text.split()

#Prepare regex for char filtering
re_punc = re.compile('[%s]' % re.escape(string.punctuation))

#remove punctuation from each words
stripped = [re_punc.sub('', w) for w in words]

#put text to lower case
stripped = [word.lower() for word in stripped]

print(stripped[:100]) 