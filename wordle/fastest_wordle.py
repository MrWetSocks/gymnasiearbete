import time

start = time.perf_counter()
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

adj = {i: [j for j in processed_words if (j|i).bit_count() == 10] for i in processed_words}

print(len([i for i in processed_words if i & (1 << 25)]))


