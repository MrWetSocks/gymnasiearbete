import time
# Read in all the words
def solve():
    start = time.perf_counter()
    words = [i for i in open('wordlist_2.txt', 'r').read().split('\n')]

    # Filter out words with duplicate characters
    filtered_words = []
    letter_combs = []
    for word in words:
        if len(word) != 5:
            continue
        # Add word if it has no duplicate characters and is not an anagram of
        # any word in filtered_words
        if len(set(word)) == 5 and set(word) not in letter_combs:
            filtered_words.append(word)
            letter_combs.append(set(word))

    five_word_combinations = []

    checked_letter_combs = set()
    for first_word in filtered_words:
        if time.perf_counter() - start >= 1800:
            break

        combinations = [[[first_word], set(first_word)]]
        for tot_words in range(4):

            new_combs = []
            for index, comb in enumerate(combinations):
                if index % 100 == 0:
                    print(index)
                chosen_words, letters = comb
                candidate_words = [word for word in filtered_words if len(set(word) | set(''.join(chosen_words))) == (len(chosen_words) + 1) * 5]
                for next_word in candidate_words:
                    unique_letters = letters | set(next_word)

                    if len(unique_letters) == (len(chosen_words) + 1)*5 and ''.join(sorted(unique_letters)) not in checked_letter_combs:
                        checked_letter_combs.add(''.join(sorted(unique_letters)))
                        new_combs.append([[*chosen_words, next_word], unique_letters])
            combinations = new_combs
            if tot_words == 3:
                combins = [i[0] for i in combinations]

                if len(combins):
                    five_word_combinations += combins

    return time.perf_counter() - start, len(five_word_combinations)
