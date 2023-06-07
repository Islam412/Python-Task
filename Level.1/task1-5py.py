'''5. Create a function that takes a sentence and prints how many words in the sentence (do not count the
spaces)'''

sentence=input('Enter sentence: ') 
def my_len(sentencez):
    return(len(sentence.split(' ')))
count= my_len(sentence)
print(count)
