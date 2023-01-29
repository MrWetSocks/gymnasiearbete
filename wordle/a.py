words = words = [i for i in open('wordlist_2.txt', 'r').read().split('\n')]

words = [i for i in words if i[0] == 'h' and all([c in 'hiresk' for c in i])]
print(words)