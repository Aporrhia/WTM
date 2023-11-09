# Word Transcription Maker (WTM)
#
# Transcribes a word into IPA (International Phonetic Alphabet) symbols
#
# This programme is designed for the Chaos language.
#
# Version: 1.0.0
#
# Author: _SpelleR_
# GitHub: Aporrhia



def transcribe(word):
    # Define the vowels and two-letter combinations
    vowels = 'aeiou'
    two_letter_combinations = {'ch': 'ʧ', 'dj': 'ʤ', 'sh': 'ʃ', 'ts': 'ʦ', 'th': 'θ'}

    # Create a mapping from letters to their IPA equivalents
    letter_to_IPA = {letters[i]: IPA[i] for i in range(len(letters))}

    # Initialize the transcribed word as an empty string
    transcribed_word = ''

    i = 0
    while i < len(word):
        # If the current and next characters form a two-letter combination, transcribe it as such
        if i < len(word) - 1 and word[i:i+2] in two_letter_combinations:
            transcribed_word += two_letter_combinations[word[i:i+2]]
            i += 2
        # If the current character is 'i' and the previous character is a vowel, transcribe it as 'ɪ'
        elif word[i] == 'i' and (i > 0 and word[i-1] in vowels):
            transcribed_word += 'ɪ'
            i += 1
        # If the current character is 'o' and the previous character is k, r, y or is the last, transcribe it as 'ɔː'
        elif word[i] == 'o' and (word[i-1] == "w" or word[i-1] == "k" or word[i-1] == "r" or word[i-1] == "y" or word[i] == len(word) - 1):
            transcribed_word += 'ɔː'
            i += 1
        # Otherwise, transcribe the character normally
        else:
            transcribed_word += letter_to_IPA[word[i]] if word[i] in letter_to_IPA else word[i]
            i += 1

    return transcribed_word

# Define the letters and their IPA equivalents

letters = ["a", "b", "ch", "d", "dj", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "sh", "t", "ts", "th", "u", "y", "w", "v"]

IPA = ["a", "b", "ʧ", "d", "ʤ","e", "f", "g", "h", "i", "ʒ", "k", "l", "m", "n", "o", "p", "r", "s", "ʃ", "t", "ʦ", "θ", "u", "'", "ʊ", "v"]

# Main loop

print("\nWelcome to the Word Transcription Machine!")
print("by _SpelleR_")
print("==========================================")
print("Enter 'x' to quit at any time.\n")

while True:
    word = input("Enter a word to transcribe:\t ").lower()

    # Check if the word contains only letters
    if not word.isalpha():
        print("Enter a word containing only letters.\n")
        continue

    # Exit the programme if the user enters 'x'
    if word == 'x':
        print("\nThank you for using the Word Transcription Machine. Goodbye!\n")
        break

    # Print the transcription of the word
    print("Transcription of the word:\t", transcribe(word), "\n")

    