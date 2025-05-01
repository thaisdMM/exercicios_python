# 8. Contador de palavras
# Peça uma frase e mostre quantas palavras ela tem (dica: use .split()).

phrase = input("Enter a phrase: ")
print(f"The phrase you entered was: {phrase.upper()}")
split_phrase = phrase.split()
all_words_together = "".join(split_phrase)

print(f"\nIncluding space, the phrase has: {len(phrase)} characters.")
print(f"Without spaces, the phrase has: {len(all_words_together)} characters.")
print(f"The phrase contains: {len(split_phrase)} words.")
