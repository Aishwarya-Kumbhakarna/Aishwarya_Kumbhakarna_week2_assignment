
'''Write a script that counts the frequency of words in a given text and stores the result in a dictionary.'''

text = input("Enter some text: ")

words = text.lower().split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nWord Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")
