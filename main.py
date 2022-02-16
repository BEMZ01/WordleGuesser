import random
import re
from pprint import pprint


def get_score(word):
    score = 0
    for x in range(len(ALPHABET)):
        score += word.count(ALPHABET[x]) * (abs(y - 28))  # give score based on frequency of common letters in alphabet
    return word_score


def display(attempts, cword):
    if len(attempts) == 0:
        return None
    else:
        print("\n\nGuess Report")
    for c in range(len(attempts)):
        print("Guess " + str(c + 1) + "/6\n")
        array = list(attempts[c])
        for x in range(len(array)):
            if cword[x] == array[x]:
                print("G\t" + str(array[x]))
            elif array[x] in cword:
                print("Y\t" + str(array[x]))
            else:
                print("N\t" + str(array[x]))


ALPHABET = ["E", "T", "A", "O", "I", "N", "S", "R", "H", "D", "L", "U", "C", "M", "F", "Y", "W", "G", "P", "B", "V",
            "K", "X", "Q", "J", "Z"]
score = []

with open("possible", "r") as file:
    file = file.readlines()
    for x in range(len(file)):
        file[x] = str(file[x]).replace("\n", "").upper()
        score.append(0.00)
for x in range(len(file)):
    word_score = 0
    for y in range(len(ALPHABET)):
        word_score += file[x].count(ALPHABET[y]) * (abs(y - 28))
        score[x] = word_score
sorted_list = [x for _, x in sorted(zip(score, file), reverse=False)]
print("Loaded words, total " + str(len(file)))
print("\n")
correct_word = random.choice(file)
#print(correct_word)
guesses = 0
inputs = []
while guesses != 6:
    display(inputs, correct_word)
    # fancy ml code
    print("Guess " + str(guesses + 1) + "/6")
    inp = input("\n:> ").upper()  # replace with fancy ml code
    inputs.append(inp)
    if inp == correct_word:
        print("Yay, game won :)")
        raise Exception("Crash")


    # if guesses = 6 end game
    # if input = correct_word end game
    guesses += 1
raise Exception("You didnt get the answer lol")