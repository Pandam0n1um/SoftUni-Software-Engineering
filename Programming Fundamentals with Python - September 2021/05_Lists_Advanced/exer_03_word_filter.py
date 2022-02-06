words_list = input().split()

even_length_words = list(filter(lambda word: len(word) % 2 == 0, words_list))

print(*even_length_words, sep = "\n")