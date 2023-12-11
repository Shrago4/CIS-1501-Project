import random

#open word lists
wordleWords = open("WordleWords.txt", "r")
guessWords = open("GuessWords.txt", "r")

#readlines in word lists
wordleLines = wordleWords.readlines()
guessLines = guessWords.readlines()

#store lines from WordleWords in fiveLetterWordleWords list
fiveLetterWordleWords = []
for line in wordleLines:
    word = line.strip()
    fiveLetterWordleWords.append(word)

#store lines from GuessWords in fiveLetterGuessWords list
fiveLetterGuessWords = []
for line in guessLines:
    word = line.strip()
    fiveLetterGuessWords.append(word)

#created function to randomize word bank
def wordleWord():
    words = random.sample(fiveLetterWordleWords, 50)
    return words

# INSTRUCTIONS
def instruction():
    print("You are playing Wordle. This is a game where the player tries to guess a 5 letter word. The player has 6 attempts to guess the word correctly. "
          "Based on the player's guess, the computer will say which letters belong in the word and whether or not they are in the correct place. "
          "✅ means the letter is correct and in the right place, ❌ means the letter is incorrect. 🟨 means the letter is correct but in the wrong place. "
          "We hope you enjoy the game!")
instruction()


# START GAME
def check():
    words = wordleWord() 
    print(words)    #prints the word bank. This is just for demo
    #The checks
    while True:
        guess = input("Please guess a word: ")      #player's guess
        if len(guess) != 5:                         # checks that the word is 5 letters
            print("Please enter a 5-letter word.")
            continue
        if guess not in fiveLetterWordleWords and guess not in fiveLetterGuessWords:        #checks that the guess word is a valid english word
            print("Please guess a valid 5-letter word")
            continue

        if guess in words:
            print("You are correct! Congrats, you win!")            #if word guessed correctly
            break
        else:

            #create open lists to store words in
            zeroCorrect = []
            oneCorrect = []
            twoCorrect = []
            threeCorrect = []
            fourCorrect = []
            fiveCorrect = []
            for word in words:
                correctLetters = 0

                #checks to see how many letters match the guess word for each word in the word bank
                for index in range(len(word)):
                    val = word[index]
                    letter = guess[index]
                    if letter in word and letter in val:
                        correctLetters += 1
                    elif letter in word:
                        correctLetters += 1
                    else:
                        correctLetters += 0

                # stores words based on how letters match
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

            #complie all lists into one list
            lists = [fiveCorrect, fourCorrect, threeCorrect, twoCorrect, oneCorrect, zeroCorrect]

            #find the list witht the most amount of letters
            maxList = list(max(lists, key = len))

            #prints words just for demo
            print(maxList)
            print("Words with 5 correct letters:", fiveCorrect)
            print("Words with 4 correct letters:", fourCorrect)
            print("Words with 3 correct letters:", threeCorrect)
            print("Words with 2 correct letters:", twoCorrect)
            print("Words with 1 correct letters:", oneCorrect)
            print("Words with 0 correct letters:", zeroCorrect)

            print("*************************************************************************************************")

            #open dictionary so we can spearte each word in the max list by which letters are correct and in the right spot
            letter_lists = {letter: [] for letter in guess}
            
            #for loop interates over pairs of words, checks if the letter and value are the same and appends to list with corresponding letter    
            for word in maxList:
                for index, (val, letter) in enumerate(zip(word, guess)):
                    if letter == val:
                        letter_lists[letter].append(word)

            # Prints the categorized lists for the demo
            for letter, word_list in letter_lists.items():
                print(f"Words with '{letter}': {word_list}")
            
            # Stores larget dictionary value in largest list
            largest_list_key = max(letter_lists, key=lambda k: len(letter_lists[k]))
            largest_list = letter_lists[largest_list_key]
            print(largest_list)

            #checking if there are velues in Largetst list, and storing them in words, so they become the set of words
            if largest_list:
                words = largest_list
                word = random.choice(largest_list)      #randomly slects one word in list to compare to gues word.

                correctPlace = [g == w for g, w in zip(guess, word)]
                correctLetters = [g for g in guess if g in word and guess.count(g) <= word.count(g)]

                for index, (g, w) in enumerate(zip(guess, word)):
                    if correctPlace[index]:
                        print(g + " ✅ ")
                    elif g in correctLetters:
                        print(g + " 🟨 ")
                    else:
                        print(g + " ❌ ")

            #if no words in larget lists, all letters are incorrect and words list diesnt change.
            else:               
                words = maxList
                for letter in guess:
                    print(letter + " ❌ ")


check()
