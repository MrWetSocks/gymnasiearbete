import time

def solve():
    start = time.perf_counter()

    # Read in all the words
    # O(w)
    words = [i for i in open('wordlist_2.txt', 'r').read().split('\n')]

    words_bitmap = {}
    processed_words = set()
    word_sets = [set()]*26

    # Filter out dictionary to five letter words with five distinct characters and removing anagrams
    # O(w)
    for word in words:
        # Ensure word length is 5
        if len(word) != 5:
            continue
        bitmap = 0

        # Convert the word to a bitmap where the bit at position 2^n is the nth letter in the alphabet
        for char in word:
            bitmap |= 1 << (ord(char)-97)

        # Ensure the word does not contain duplicate letters
        if bitmap.bit_count() == 5:
            # O(1)
            if bitmap not in words_bitmap:
                words_bitmap[bitmap] = []

            words_bitmap[bitmap].append(word)
            processed_words.add(bitmap)

    # Find the least common characters in each word
    freq = [0]*26
    # O(w)
    for word in processed_words:
        for bit in range(26):
            if word & (1 << bit):
                freq[bit] += 1
                word_sets[bit].add(word)
    freq = freq[:]

    least_freq = freq.index(min(freq))
    freq.pop(least_freq)
    next_least = freq.index(min(freq))
    next_least += next_least >= least_freq

    five_word_combinations = []
    checked_combs = set()

    # Try every word containing either the least common or next least common character as the first word
    # O(w) + O(w)
    for ind, first_word in enumerate({i for i in processed_words if i & ((1 << least_freq) | (1 << next_least))}):

        # Length: w^n where n == combination length
        combinations = [[[first_word], first_word]]

        for tot_words in range(4):
            new_combs = []

            # O(w^n)
            for comb in combinations:
                chosen_words, letters = comb
                # O(w)
                candidate_words = [word for word in processed_words if not word & letters]

                # O(w)
                for next_word in candidate_words:

                    unique_letters = letters | next_word

                    # Check if we have already found the specific combination of letters
                    if unique_letters not in checked_combs:
                        new_combs.append([[*chosen_words, next_word], unique_letters])
                        checked_combs.add(unique_letters)
            combinations = new_combs
            if tot_words == 3:
                # O(w)
                combins = [i[0] for i in combinations]

                if len(combins):
                    five_word_combinations += combins

    with open('fast_wordle.txt', 'w') as f:
        for combination in five_word_combinations:
            ws = ['|'.join(words_bitmap[i]) for i in combination]
            f.write(' '.join(ws) + '\n')

    return time.perf_counter() - start, len(five_word_combinations)

def conv_word(word):
    return '|'.join(words_bitmap[word])
def get_candidates(words):
    candidates = set() | processed_words

    for bit in range(26):
        if words & (1 << bit):
            candidates -= word_sets[bit]

    return candidates