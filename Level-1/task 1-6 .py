'''Create a function that takes a sentence and word and remove the word from the sentence'''
sentence = 'Hello Geeks for geeks'
words = list(filter(lambda word: not any(char.isdigit()
										for char in word), sentence.split()))
print(words) # Output: ['Hello', 'Geeks', 'for', 'geeks']
