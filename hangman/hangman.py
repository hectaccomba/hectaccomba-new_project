import random
words_list = open('words.txt').read().splitlines()

word = random.choice(words_list)

print(word)
