# Task 1

# Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
# and the number of occurrences as values.



sentence = input("Some sentence: ")

words = sentence.split(' ')

sentence_dict = {}

# print(sentence)
# print(words)

for word in words:
    if word in sentence_dict:
        sentence_dict[word] += 1
    else:
        sentence_dict[word] = 1

print(sentence_dict)
