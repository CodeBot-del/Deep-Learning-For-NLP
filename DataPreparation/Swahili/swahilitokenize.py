import regex as re  
import string  

#load text 
filename = 'ushauri.txt' 
file = open(filename, 'rt') 
text = file.read()
file.close() 

#split into words by whitespace
words = text.split() 

# print(words[:100])

#prepare regex for char filtering...it does remove punctuations
re_punc = re.compile('[%s]' % re.escape(string.punctuation))

#remove all punctuation from each word 
stripped = [re_punc.sub('', w) for w in words] 

#put text to lower case 
stripped = [word.lower() for word in stripped]

print(stripped[:100])
