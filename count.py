from collections import Counter
words = ['Yes', 'but', 'no', 'but', 'Yes']
wordcount = Counter(words)
print(wordcount['Yes'])
print(wordcount.most_common())
