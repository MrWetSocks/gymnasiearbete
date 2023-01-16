
# Read in all the words
words = [i for i in open('wordlist.txt', 'r').read().split('\n')]

print(f"Total words: {len(words)}")

# Filter out words with duplicate characters
words_bitmap = {}
processed_words = set()
word_sets = [set()]*26

for word in words:
    if len(word) != 5:
        continue
    bitmap = 0

    for char in word:
        bitmap |= 1 << (ord(char)-97)

    if bitmap.bit_count() == 5:
        if bitmap not in words_bitmap:
            words_bitmap[bitmap] = []

        words_bitmap[bitmap].append(word)
        processed_words.add(bitmap)

print(f"Filtered words: {len(processed_words)}")

for word in processed_words:
    for bit in range(26):
        if not word & (1 << bit):
            word_sets[bit].add(word)


five_word_combinations = []
checked_combs = set()

def conv_word(word):
    return '|'.join(words_bitmap[word])

def get_candidates(words):
    candidates = processed_words.copy()

    for bit in range(26):
        if words & (1 << bit):
            candidates -= word_sets[bit]

    return candidates

for ind, first_word in enumerate(processed_words):
    combinations = [[[first_word], first_word]]

    for tot_words in range(4):
        print(f"Finding all combinations of {tot_words+2} words with starting word \"{conv_word(first_word)}\" (index {ind})")

        new_combs = []
        for comb in combinations:
            chosen_words, letters = comb
            candidate_words = get_candidates(letters)
            for next_word in candidate_words:
                unique_letters = letters | next_word

                if unique_letters not in checked_combs:
                    new_combs.append([[*chosen_words, next_word], unique_letters])
                    checked_combs.add(unique_letters)
        combinations = new_combs
        print(f"{len(combinations)} combinations of {tot_words+2} words starting with word \"{conv_word(first_word)}\"\n")
        if tot_words == 3:
            combins = [i[0] for i in combinations]

            if len(combins):
                five_word_combinations += combins
                print("Five word combination found: ", *combins, sep='\n')


for comb in five_word_combinations:
    wrd = ', '.join([conv_word(word) for word in comb])
    print(wrd)
# print(five_word_combinations)