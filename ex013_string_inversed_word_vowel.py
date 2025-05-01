# 4. Inversor de string
# Peça uma palavra e mostre ela invertida (ex: “python” → “nohtyp”).

# FATIAMENTO

print("FATIAMENTO")
word = input("Enter a word: ")
print(f"Word: {word}")
print(f"Word wiritten backwards: {word[::-1]}")

# FOR

print("\nFOR")
inverse = ""
word = input("Enter a word: ")
for i in range(len(word) - 1, -1, -1):
    inverse += word[i]
print(inverse)

# REVERSED()

print("\nREVERSED()")
word = input("Enter a word: ").strip().lower()
for letter in reversed(word):
    print(letter, end="")

# REVERSING ONLY THE VOWELS OF THE WORD

print("\nFOR, FATIAMENTO: REVERSING ONLY THE VOWELS OF THE WORD")
# Coletar todas as vogais
word = input("Enter a word: ").strip().lower()
have_vowel = ""
for letter in word:
    if letter in "aeiou":
        have_vowel += letter

# Inverter as vogais
inverse = have_vowel[::-1]

# Montar nova palavra
new_word = ""
vowel_index = 0  # Para acessar as vogais invertidas

for letter in word:
    if letter in "aeiou":
        new_word += inverse[vowel_index]
        vowel_index += 1  # Avança para a próxima vogal invertida
    else:
        new_word += letter  # Mantém a consoante

print(f"Original word: {word}")
print(f"Vowels (original): {have_vowel}")
print(f"Vowels (reversed): {inverse}")
print(f"Word with vowels reversed: {new_word}")
