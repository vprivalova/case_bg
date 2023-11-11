unique_words = []
all_words = []

with open('input_txt', 'r', encoding='utf-8') as file:
    for paragraph in file:
        words = paragraph.split()
        for word in words:
            if word == '-' or word == '–':
                words.remove(word)
        all_words.extend(words)

for word in all_words:
    if word in unique_words:
        continue
    else:
        unique_words.append(word)

list_words = {}
for word in unique_words:
    list_words[word] = []
    if word in list_words:
        per = unique_words.index(word)
        list_words.update({word: unique_words[per+1:]})
    else:
        continue