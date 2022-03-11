import random
import re
from pprint import pprint


def ai(word_list, previous_words, previous_words_info=None):
    # using computer magic and wizardry; make computer choose what the word is
    doesnt_contain = []
    yellow_contain = []
    green_contain = []
    try:
        with open("storage/ai", "r") as file:
            file = file.readlines()
            doesnt_contain = file[0].replace("\n", "").split("|")
            yellow_contain = file[1].replace("\n", "").split("|")
            temp = file[2].replace("\n", "").split("|")
            for x in range(len(temp)):
                green_contain.append(temp[x].split("-"))
    except IndexError:
        pass

    print(doesnt_contain, yellow_contain, green_contain)
    if previous_words_info is None:
        return random.choice(word_list[random.randint(0, int(len(word_list)/2)):int(len(word_list))])
    for x in range(len(previous_words_info)):
        word = previous_words_info[x]
        for y in range(len(word)):
            if word[y] == "N":
                if previous_words[x][y] not in doesnt_contain:
                    doesnt_contain.append(previous_words[x][y])
            elif word[y] == "Y":
                if previous_words[x][y] not in yellow_contain:
                    yellow_contain.append(previous_words[x][y])
            elif word[y] == "G":
                if previous_words[x][y] not in green_contain:
                    green_contain.append([previous_words[x][y], y])




    with open("storage/ai", "w") as file:
        out = ""
        for x in [doesnt_contain, yellow_contain]:
            for word in x:
                out = out+word+"|"
            out = out.rstrip(out[-1])+"\n"
        for word in green_contain:
            out = out + str(word[0]) + "-" + str(word[1]) + "|"
        out = out.rstrip(out[-1]) + "\n"
        file.write(out)
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

with open("storage/ai", "w+") as file:
    pass

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

print("Loaded words, total " + str(len(file)))
print("\n")
correct_word = random.choice(file)
print(correct_word)
guesses = 0
inputs = []
while guesses != 6:
    history = display(inputs, correct_word)
    print("Guess " + str(guesses + 1) + "/6")
    print("AI suggestion: "+str(ai(sorted_list, inputs, history)))
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