words = ["white", "red", "white", "pink", "red", "white"]
unique_words = list(set(words))
word_count = {}
for word in unique_words:
    word_count[word] = words.count(word)
print("Unique words:", unique_words)
print("Word frequencies:", word_count)
