#4. Create a function that takes a sentence and prints the sentence without duplicated words
def sentence_without_duplicate(sentence):
    words = sentence.split(' ')
    new_words =[]
    for w in words:
        if w in new_words:
            continue
        else:
            new_words.append(w)
    print(new_words)



sentence_without_duplicate('hello hello hello world world world')
