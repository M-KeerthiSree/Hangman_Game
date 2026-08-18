import random
words=["apple","avocado","mango","blueberry","guava"]
lives=6      # no of incorrect guesses allowed
word=random.choice(words)
guessed_letters=[]
guessed_word=["_"]*len(word)

print("====== HANGMAN GAME ======")

while lives > 0 and "_" in guessed_word:
    print("word : "," ".join(guessed_word))
    print("Lives Left : ",lives)
    letter=input("Enter a letter : ").lower()

    #checking if the input is valid or not
    if len(letter)!=1 or not letter.isalpha():
        print("Invalid Entry")
        continue

# if the letter is already entered
    if letter in guessed_letters:
        print("You already entered that letter. ")
        continue
    guessed_letters.append(letter)

    #to check if the letter is in word or not
    if letter in word:
        print("Correct")

        for i in range(len(word)):
            if word[i]==letter:
                guessed_word[i]=letter
    else:
        print("Wrong")
        lives-=1
if "_" not in guessed_word:
    print("\nCongratulations ! You guessed correct word : \n",word)
else:
    print("\n Game Over")
    print("The word was",word)
