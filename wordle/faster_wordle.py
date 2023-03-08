import time

# Variables
# w - words
def solve():
    start = time.perf_counter()
    # Read in all the words

    # O(w)
    words = [i for i in open('wordlist_2.txt', 'r').read().split('\n')]

    # Filter out words with duplicate characters
    words_bitmap = {}
    processed_words = set()
    word_sets = [set()]*26

    # O(w)
    for word in words:
        if len(word) != 5:
            continue
        bitmap = 0

        # O(1)
        for char in word:
            bitmap |= 1 << (ord(char)-97)

        if bitmap.bit_count() == 5:
            # O(1)
            if bitmap not in words_bitmap:
                words_bitmap[bitmap] = []

            words_bitmap[bitmap].append(word)
            processed_words.add(bitmap)


    freq = [0]*26
    # O(w)
    for word in processed_words:
        for bit in range(26):

            if word & (1 << bit):
                freq[bit] += 1
                word_sets[bit].add(word)
    freq = freq[:]
    # O(w)
    least_freq = freq.index(min(freq))
    freq.pop(least_freq)

    # O(w)
    next_least = freq.index(min(freq))
    next_least += next_least >= least_freq

    # O(w^2)
    adj = {i: {j for j in processed_words if not j & i} for i in processed_words}


    five_word_combinations = []
    visited = set()

    # O(w)
    for i in {j for j in processed_words if j | ((1 << least_freq) | (1 << next_least))}:
        q = [[[i], i]]

        # O(w^5)
        while q:
            words, letters = q.pop()
            if len(words) == 5:
                five_word_combinations.append(words)
                continue

            # O(min(len(adj[i]))
            candidates = set.intersection(*[adj[i] for i in words])

            # O(w)
            for candidate in candidates:
                unique_letters = letters | candidate

                # O(1)
                if unique_letters not in visited:
                    visited.add(unique_letters)
                    q.insert(0, [[*words, candidate], unique_letters])

    with open('faster_wordle.txt', 'w') as f:
        # O(w)
        for combination in five_word_combinations:
            # O(w)
            ws = ['|'.join(words_bitmap[i]) for i in combination]
            f.write(' '.join(ws) + '\n')


    return time.perf_counter() - start, len(five_word_combinations)