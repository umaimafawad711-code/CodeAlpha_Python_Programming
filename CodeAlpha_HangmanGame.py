import random
words = ["python", "internship", "hangman", "program", "developer"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("🎯 Welcome to CodeAlpha Hangman!")
print("Guess the word:", " ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue
    if guess in used_letters:
        print("You already guessed that letter.")
        continue

    used_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct:", " ".join(guessed))
    else:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")

if "_" not in guessed:
    print(f"🎉 You win! The word was '{word}'.")
else:
    print(f"💀 Out of attempts! The word was '{word}'.")
