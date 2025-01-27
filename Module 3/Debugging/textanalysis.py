"""
Program: textanalysis.py
Author: Ken (Fixed by Cash Kiefer)
Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file.
"""

# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

# Count the sentences
sentences = text.count('.') + text.count('?') + \
text.count(':') + text.count(';') + \
text.count('!')

# Count the words
words = len(text.split())

# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    word_syllables = 0
    # Flag to track if the previous character was a vowel
    previous_was_vowel = False
    
    for char in word:
        if char in vowels:
            # Count the vowel only if the previous character was not a vowel
            if not previous_was_vowel:
                word_syllables += 1
                previous_was_vowel = True
        else:
            previous_was_vowel = False
    
    # Handle special cases like 'es', 'ed', 'e' endings
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            word_syllables -= 1
    
    # Handle 'le' ending by adding an extra syllable
    if word.endswith('le'):
        word_syllables += 1

    # Add the syllables for the current word to the total syllable count
    syllables += word_syllables

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
(syllables / words) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")
