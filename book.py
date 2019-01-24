import re               #regular expressions
import collections      #allows us to count occurances of words

text = open('book.txt').read().lower()              #read method..lower case. contents of book.txt have been read into                                                   string called text
words = re.findall('\w+', text)                     #findall method is used to pass the string and find words 
                                                    #w denotes anything not a whitespace. + denotes 1 or more
                                                    #every occurance of 1+ characters is a word(no whitespaces)
print(collections.Counter(words).most_common(10))   #regular expressions findall method and text string. counter                                            method counts occurances. most_common method limits results to 10 words 