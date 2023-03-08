import time

def solve():
    start = time.perf_counter()
    # Read in all the words
    words = [i for i in open('wordlist_2.txt', 'r').read().split('\n')]

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

    def conv_word(word):
        return '|'.join(words_bitmap[word])


    freq = [0]*26
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


    adj = {i: {j for j in processed_words if not j & i} for i in processed_words}


    five_word_combinations = []
    visited = set()

    for i in {j for j in processed_words if j | ((1 << least_freq) | (1 << next_least))}:
        q = [[[i], i]]
        while q:
            words, letters = q.pop()
            if len(words) == 5:
                five_word_combinations.append(words)
                continue
            candidates = set.intersection(*[adj[i] for i in words])

            for candidate in candidates:
                unique_letters = letters | candidate
                if unique_letters not in visited:
                    visited.add(unique_letters)
                    q.insert(0, [[*words, candidate], unique_letters])

    with open('faster_wordle.txt', 'w') as f:
        for combination in five_word_combinations:
            ws = ['|'.join(words_bitmap[i]) for i in combination]
            f.write(' '.join(ws) + '\n')


    return time.perf_counter() - start, len(five_word_combinations)