# 1. Contador de vogais
# Peça uma palavra e mostre quantas vogais ela tem.

word = input("Type a word: ").strip().lower()

print(
    f"""
In the word {word} we have:
{word.count('a')} a vowels
{word.count('e')} e vowels
{word.count('i')} i vowels
{word.count('o')} o vowels
{word.count('u')} u vowels
"""
)
total = (
    word.count("a")
    + word.count("e")
    + word.count("i")
    + word.count("o")
    + word.count("u")
)
print(f"Total vowels = {total}")

