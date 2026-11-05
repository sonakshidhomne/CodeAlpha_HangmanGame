
import random

words = ["python", "apple", "computer", "school", "gaming"]

word = random.choice(words)
guessed = []
wrong = 0
max_wrong = 6

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the hidden word!")
print("You have 6 wrong attempts.\n")

while wrong < max_wrong:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)
    print("Wrong guesses:", wrong, "/", max_wrong)

    if all(letter in guessed for letter in word):
        print("\nCongratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!\n")
        continue

    if guess in guessed:
        print("You already guessed this letter!\n")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct guess!\n")
    else:
        wrong += 1
        print("Wrong guess!\n")

else:
    print("Game Over!")
    print("The correct word was:", word)

print("\nThanks for playing!")
