import random

unique_words = []
SIGNS = '.!?'
all_words = []

with open('input_txt', 'r', encoding='utf-8') as file1:
    number = file1.readline()

    for paragraph in file1:
        words = paragraph.split()

        for word in words:
            if word == '-' or word == '–':
                words.remove(word)

        all_words.extend(words)

for word in all_words:
    if word not in unique_words:
        unique_words.append(word)

following_words = []
second_list = []
amount = 0

for elem in unique_words:
    amount = all_words.count(elem)
    all_words_2 = all_words.copy()

    for i in range(amount):
        index = all_words_2.index(elem)

        if index != len(all_words) - 1:
            following_words.append(all_words_2[index+1])
            all_words_2[index] = all_words_2[index].replace(all_words_2[index], '+')

    following_words_2 = following_words.copy()
    second_list.append(following_words_2)
    following_words.clear()

bred = []
bred_line = ''

for j in range(int(number)):
    beg = random.randint(0, len(unique_words) - 1)

    while unique_words[beg][0].isupper() is False:
        beg = random.randint(0, len(unique_words) - 1)

    bred_line = bred_line + unique_words[beg]

    index = beg
    end = random.randint(0, len(second_list[index]) - 1)

    while second_list[index][end][-1] not in SIGNS:
        bred_line = bred_line + ' ' + second_list[index][end]
        index = unique_words.index(second_list[index][end])
        end = random.randint(0, len(second_list[index]) - 1)

    bred_line = bred_line + ' ' + second_list[index][end]
    bred.append(bred_line)
    bred_line = ''


with open('output_txt', 'w', encoding='utf-8') as file2:
    file2.write(number)
    for elem in bred:
        file2.write(elem + '\n')
