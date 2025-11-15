###
# Counts vowels in the text
#
text = "Szymon"
vowels = "aeiouAEIOU"
vowel_count = 0

idx = 0
# Count vowels in the text
while idx < len(text):
    char = text[idx]
    if char in vowels:
        vowel_count += 1
    idx += 1

print(f"The number of vowels in the text is: {vowel_count}")