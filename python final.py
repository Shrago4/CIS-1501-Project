import random

wordleWords = open("WordleWords.txt", "r")
guessWords = open("GuessWords.txt", "r")

wordleLines = wordleWords.readlines()
guessLines = guessWords.readlines()

fiveLetterWordleWords = []
for line in wordleLines:
    word = line.strip()
    fiveLetterWordleWords.append(word)

fiveLetterGuessWords = []
for line in guessLines:
    word = line.strip()
    fiveLetterGuessWords.append(word)

def wordleWord():
    word = random.choice(fiveLetterWordleWords)
    return word


# INSTRUCTIONS
def instruction():
    print("You are playing Wordle. This is a game where the user tries to guess a 5 letter word. The user has 6 attempts to guess the word correctly. "
          "Based on the user's guess, the computer will say which letters belong in the word and whether or not they are in the correct place. "
          "✅ means the letter is correct and in the right place, ❌ means the letter is incorrect. 🟨 means the letter is correct but in the wrong place. "
          "We hope you enjoy the game!")
instruction()


# START GAME
def check():
    word = wordleWord() 
    print(word)   #prints the secret word. Have to delete 
    tries = 6
    while tries > 0:
        guess = input("Please guess a word: ")
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        if guess not in fiveLetterWordleWords and guess not in fiveLetterGuessWords:
            print("Please guess a valid 5-letter word")
            continue
        if guess == word:
            print("You are correct! Congrats, you win!")
            break
        else:
            tries -= 1
            print("That is incorrect. You have", tries, "tries left.")
            correctPlace = [g == w for g, w in zip(guess, word)]
            correctLetters = [g for g in guess if g in word and guess.count(g) <= word.count(g)]

            for index, (g, w) in enumerate(zip(guess, word)):
                if correctPlace[index]:
                    print(g + " ✅ ")
                elif g in correctLetters:
                    print(g + " 🟨 ")
                else:
                    print(g + " ❌ ")
            if tries == 0:
                print("The word was", word)


check()
