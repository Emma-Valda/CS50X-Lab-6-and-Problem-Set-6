# A program to calculate the grade level of a given text

from cs50 import get_string

s = get_string("Text: ")
words, letters, sentences = 0, 0, 0


# Iterate over every letter in the given string
# Number of words:
for i in range(len(s)):
    if (i == 0 and s[i] != ' ') or (i != len(s) - 1 and s[i] == ' ' and s[i + 1] != ' '):
        words += 1
    # Number of letters:
    if s[i].isalpha():
        letters += 1
    # Number of sentences:
    if s[i] == '.' or s[i] == '?' or s[i] == '!':
        sentences += 1


# Used Coleman-Liau index formula to calculate the index,
# where L is the average number of letters per 100 words in the text,
# and S is the average number of sentences per 100 words in the text.
# L and S will be a floating point numbers
L = letters / words * 100
S = sentences / words * 100
# Converting index from a floating point number into an integer
index = round(0.0588 * L - 0.296 * S - 15.8)


if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
