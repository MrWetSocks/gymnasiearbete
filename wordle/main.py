
# Read in all the words
words = [i for i in open('wordlist.txt', 'r').read().split('\n')]

print(f"Total words: {len(words)}")

# Filter out words with duplicate characters
filtered_words = []
letter_combs = set()
for word in words:
    if len(word) != 5:
        continue
    # Add word if it has no duplicate characters and is not an anagram of
    # any word in filtered_words
    if all(word.count(char) == 1 for char in word) and ''.join(sorted(word)) not in letter_combs:
        filtered_words.append(word)
        letter_combs.add(''.join(sorted(word)))

print(f"Filtered words: {len(filtered_words)}")

word_combinations = [[[word], set(word)] for word in filtered_words]


# print(f"Total words: {len(filtered_words)}")
for i in range(4):
    new_combinations = []
    letter_combs = set()
    print(f"Current combinations of {i+1} words with unique letters: {len(word_combinations)}")
    for index, word in enumerate(filtered_words):
        if index % 100 == 0:
            print(len(new_combinations))
            print(index)
        for combination, letters_used in word_combinations:
            new_combination = letters_used | set(word)
            sorted_chars = ''.join(sorted(new_combination))
            print(sorted_chars in letter_combs)
            if len(new_combination) == (i+2)*5 and sorted_chars not in letter_combs:
                new_combinations.append([combination + [word], new_combination])
                letter_combs.add(sorted_chars)

    word_combinations = new_combinations

print(word_combinations)


# print(word_combinations)