text = input("Text: ")
# testing
print(text)
word = text.split()
word.sort()
# testing
print(word)
word_to_frequency = {}
for words in word:
    # check if word is a key or not
    if words in word_to_frequency:
        word_to_frequency[words] += 1
    else:  # new key
        word_to_frequency[words] = 1
# max length of words - list comprehension
max_length = max((len(words) for words in word))
for words in word_to_frequency:
    print(f"{words:{max_length}} {word_to_frequency[word]}")