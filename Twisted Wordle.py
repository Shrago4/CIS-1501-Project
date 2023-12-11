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
    words = random.sample(fiveLetterWordleWords, 50)
    return words

# INSTRUCTIONS
def instruction():
    print("You are playing Twisted Wordle. This is a game where the user tries to guess a 5 letter word. The user has unlimited attempts to guess the word correctly. "
          "Based on the user's guess, the computer will say which letters belong in the word and whether or not they are in the correct place. However since this game is a little 'twisted', the computer might not be telling the truth."
          "✅ means the letter is correct and in the right place, ❌ means the letter is incorrect. 🟨 means the letter is correct but in the wrong place. "
          "We hope you enjoy the game (and try not to get too frustrated)!")
instruction()


# START GAME
def check():
    words = wordleWord() 
    while True:
        guess = input("Please guess a word: ")
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        if guess not in fiveLetterWordleWords and guess not in fiveLetterGuessWords:
            print("Please guess a valid 5-letter word")
            continue

        if guess in words:
            print("You are correct! Congrats, you win!")
            break
        else:            
            zeroCorrect = []
            oneCorrect = []
            twoCorrect = []
            threeCorrect = []
            fourCorrect = []
            fiveCorrect = []
            for word in words:
                correctLetters = 0
                for index in range(len(word)):
                    val = word[index]
                    letter = guess[index]
                    if letter in word and letter in val:
                        correctLetters += 1
                    elif letter in word:
                        correctLetters += 1
                    else:
                        correctLetters += 0
                if correctLetters == 5:
                    fiveCorrect.append(word)
                if correctLetters == 4:
                    fourCorrect.append(word)
                if correctLetters == 3:
                    threeCorrect.append(word)
                if correctLetters == 2:
                    twoCorrect.append(word)
                if correctLetters == 1:
                    oneCorrect.append(word)
                if correctLetters == 0:
                    zeroCorrect.append(word)
            lists = [fiveCorrect, fourCorrect, threeCorrect, twoCorrect, oneCorrect, zeroCorrect]
            maxList = list(max(lists, key = len))
#**********************************************************************************************************8
            letter_lists = {letter: [] for letter in guess}

            for word in maxList:
                for index, (val, letter) in enumerate(zip(word, guess)):
                    if letter == val:
                        letter_lists[letter].append(word)

            
            # Assuming letter_lists has been generated from the previous code
            largest_list_key = max(letter_lists, key=lambda k: len(letter_lists[k]))
            largest_list = letter_lists[largest_list_key]
            
            if largest_list:
                words = largest_list
                word = random.choice(largest_list)

                correctPlace = [g == w for g, w in zip(guess, word)]
                correctLetters = [g for g in guess if g in word and guess.count(g) <= word.count(g)]

                for index, (g, w) in enumerate(zip(guess, word)):
                    if correctPlace[index]:
                        print(g + " ✅ ")
                    elif g in correctLetters:
                        print(g + " 🟨 ")
                    else:
                        print(g + " ❌ ")
            else:
                words = maxList
                for letter in guess:
                    print(letter + " ❌ ")


check()
