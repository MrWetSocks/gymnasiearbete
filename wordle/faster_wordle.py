import time

# Variables
# w - words
# c - characters

# Complexities
# Preprocessing: (w, wc + wlogc, w, w^2, w) = w^2 + 5w
# Running: preprocessing + w^6 + w^8 = w^6 + w^8 + w^2 + 5w
# Space: 2w^5 + 2w^2 + 30w
def solve():
    start = time.perf_counter()
    # Read in all the words

    # O(w)
    words = [i for i in open('wordlist_2.txt', 'r').read().split('\n')]

    # Filter out words with duplicate characters
    words_bitmap = {}  # O(w^2)
    processed_words = set()  # O(w)

    # Size: 26w
    word_sets = [set()]*26  # O(26w)

    # O(w)
    for word in words:
        if len(word) != 5:
            continue
        bitmap = 0

        # O(c)
        for char in word:
            bitmap |= 1 << (ord(char)-97)

        # O(log c)
        if bitmap.bit_count() == 5:
            # O(1)
            if bitmap not in words_bitmap:
                words_bitmap[bitmap] = []

            words_bitmap[bitmap].append(word)
            processed_words.add(bitmap)


    freq = [0]*26  # O(1)
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

    # O(w^2)
    adj = {i: {j for j in processed_words if not j & i} for i in processed_words}  # O(w^2)


    five_word_combinations = []  # O(w^5)
    visited = set()  # O(2^26)

    # O(w)
    first_words = {j for j in processed_words if j & ((1 << least_freq) | (1 << next_least))}  # O(w)

    # O(w)
    for i in first_words:
        q = [[[i], i]]  # O(w^5)

        # O(w^5)
        while q:
            words, letters = q.pop()
            if len(words) == 5:
                five_word_combinations.append(words)
                continue

            # O(min(len(adj[i]))
            candidates = set.intersection(*[adj[i] for i in words])  # O(w)

            # O(w)
            for candidate in candidates:
                unique_letters = letters | candidate

                # O(1)
                if unique_letters not in visited:
                    visited.add(unique_letters)
                    # O(w)
                    q.insert(0, [[*words, candidate], unique_letters])

    with open('faster_wordle.txt', 'w') as f:
        # O(w)
        for combination in five_word_combinations:
            # O(w)
            ws = ['|'.join(words_bitmap[i]) for i in combination]
            f.write(' '.join(ws) + '\n')

    return time.perf_counter() - start, len(five_word_combinations)


s = time.perf_counter()
solve()
print(time.perf_counter() - s)