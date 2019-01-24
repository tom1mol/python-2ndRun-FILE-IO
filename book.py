import re               #regular expressions
import collections      #allows us to count occurances of words

text = open('book.txt').read().lower()     #read method..lower case. string called text
words = re.findall('\w+', text)             
print(collections.Counter(words).most_common(10))   #regular expressions findall method and text string