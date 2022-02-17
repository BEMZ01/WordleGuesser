import random
import re
from pprint import pprint


def ai(word_list, previous_words=None):
    # using regular expressions, attempt to guess the word upon smart things
    if previous_words == None:
        return random.choice(word_list[random.randint(0, int(len(word_list)/2)):int(len(word_list))])
    return 0

def get_score(word):
    score = 0
    for x in range(len(ALPHABET)):
        print(word, score)
        score += word.count(ALPHABET[x]) * (abs(y - 28))  # give score based on frequency of common letters in alphabet
    return word_score


def display(attempts, cword):
    if len(attempts) == 0:
        return None
    else:
        print("\n\nGuess Report")
    words = []
    for c in range(len(attempts)):
        words.append([])
        print("Guess " + str(c + 1) + "/6\n")
        array = list(attempts[c])
        for x in range(len(array)):
            if cword[x] == array[x]:
                print("G\t" + str(array[x]))
                words[c].append("G")
            elif array[x] in cword:
                print("Y\t" + str(array[x]))
                words[c].append("Y")
            else:
                print("N\t" + str(array[x]))
                words[c].append("N")
    return words

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
sorted_list = [x for _, x in sorted(zip(score, file), reverse=True)]
print(sorted_list)
print("Loaded words, total " + str(len(file)))
print("\n")
correct_word = random.choice(file)
#print(correct_word)
guesses = 0
inputs = []
while guesses != 6:
    history = display(inputs, correct_word)
    print(history)
    print(correct_word)
    print("Guess " + str(guesses + 1) + "/6")
    # fancy ml code
    inp = input("\n:> ").upper()  # replace with fancy ml code
    # end fancy ml code
    inputs.append(inp)
    if inp == correct_word:
        print("Yay, game won :)")
        raise Exception("Crash")


    # if guesses = 6 end game
    # if input = correct_word end game
    guesses += 1
raise Exception("You didnt get the answer lol")