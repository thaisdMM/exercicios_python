# 7. Caça-palavra
# Peça uma frase e uma letra. Diga quantas vezes essa letra aparece na frase.

phrase = input("Enter a phrase: ").strip().lower()
find_letter = input("Choose a letter to search in the phrase: ").strip().lower()
have_letter = phrase.count(find_letter)
first_appearence_phrase = phrase.find(find_letter)
print(f"We have the letter {find_letter} {have_letter} times in the phrase.")
print(
    f"The first appearence of the letter {find_letter} in the phrase is: {first_appearence_phrase + 1}"
)
