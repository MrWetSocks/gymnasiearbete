
# Read in all the words
words = [i for i in open('wordlist_2.txt', 'r').read().split('\n')]

print(f"Total words: {len(words)}")

# Filter out words with duplicate characters
words_bitmap = {
}
processed_words = set()

for word in words:
    bitmap = 0

    for char in word:
        bitmap |= 1 << (ord(char)-97)

    if bitmap.bit_count() == 5:
        if bitmap not in words_bitmap:
            words_bitmap[bitmap] = []

        words_bitmap[bitmap].append(word)
        processed_words.add(bitmap)

print(f"Filtered words: {len(processed_words)}")

five_word_combinations = []
checked_combs = set()
# 24006 3 word combs
for first_word in {10562}:
    combinations = [[[first_word], first_word]]

    for tot_words in range(4):
        print(f"Finding all combinations of {tot_words+2} words with starting word \"{first_word}\"")

        new_combs = []
        for index, comb in enumerate(combinations):
            if index % 100 == 0:
                print(index)
            chosen_words, letters = comb
            candidate_words = [word for word in processed_words if (letters | word).bit_count() == (tot_words+2)*5]
            for next_word in candidate_words:
                unique_letters = letters | next_word

                if unique_letters.bit_count() == (tot_words+2)*5 and unique_letters not in checked_combs:
                    new_combs.append([[*chosen_words, next_word], unique_letters])
                    checked_combs.add(unique_letters)
        combinations = new_combs
        print(f"{len(combinations)} combinations of {tot_words+2} words starting with word \"{first_word}\"")
        if tot_words == 3:
            combins = [i[0] for i in combinations]

            if len(combins):
                five_word_combinations += combins
            print("Five word combinations found: ", *combins, sep='\n')


for comb in five_word_combinations:
    wrd = ', '.join(['|'.join(words_bitmap[word]) for word in comb])
    print(wrd)
# print(five_word_combinations)