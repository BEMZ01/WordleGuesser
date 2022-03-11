#############################
#                           #
#  COPYRIGHT BEMZlabs 2022  #
#    See LICENSE.MD for     #
#         more info         #
#                           #
#############################


"""
Don't worry too much about the scary copyright at the top, it just allows me to claim that this is my work!
If you are unsure weather your use falls out of the copyright license please email me (hello@bemz.info).
"""

import random
import sys
import os


def ai(word_list, scores, previous_words, previous_words_info=None):
    # using computer magic and wizardry; make computer choose what the word is
    doesnt_contain = []
    yellow_contain = []
    green_contain = []
    try:
        with open("storage/ai", "r") as file:
            file = file.readlines()
            doesnt_contain = file[0].replace("\n", "").split("|")
            temp = file[1].replace("\n", "").split("|")
            for x in range(len(temp)):
                yellow_contain.append(temp[x].split("-"))
            temp = file[2].replace("\n", "").split("|")
            for x in range(len(temp)):
                green_contain.append(temp[x].split("-"))
    except IndexError:
        pass

    if previous_words_info is None:
        return random.choice(word_list[random.randint(0, int(len(word_list) / 2)):int(len(word_list))])

    for x in range(len(previous_words_info)):
        word = previous_words_info[x]
        for y in range(len(word)):
            if word[y] == "N":
                if previous_words[x][y] not in doesnt_contain:
                    doesnt_contain.append(previous_words[x][y])
            elif word[y] == "Y":
                if [previous_words[x][y], y] not in yellow_contain:
                    yellow_contain.append([previous_words[x][y], y])
            elif word[y] == "G":
                if [previous_words[x][y], y] not in green_contain:
                    green_contain.append([previous_words[x][y], y])

    possible_words = []
    possible_words_score = []
    for x in range(len(word_list)):  # THE WORD
        score = 0
        if word_list[x] in previous_words:
            score -= 100
        for no in doesnt_contain:
            if no in word_list[x]:
                score -= 2
        for yellow in yellow_contain:
            if yellow[0] in word_list[x]:
                if yellow[0] != word_list[x][int(yellow[1])]:
                    score += 5
                else:
                    score -= 10
        for green in green_contain:
            if green[0] == word_list[x][int(green[1])]:
                score += 25
        if score > 1:
            possible_words.append(word_list[x])
            possible_words_score.append(score)

    with open("storage/ai", "w") as file:
        out = ""
        for word in doesnt_contain:
            out = out + word + "|"
        out = out.rstrip(out[-1]) + "\n"
        for x in [green_contain, yellow_contain]:
            for word in x:
                out = out + str(word[0]) + "-" + str(word[1]) + "|"
            out = out.rstrip(out[-1]) + "\n"
        file.write(out)
    sorted_words = [x for _, x in sorted(zip(possible_words_score, possible_words), reverse=True)]
    if len(sorted_words) == 0:
        return random.choice(word_list[random.randint(0, int(len(word_list) / 2)):int(len(word_list))])
    highest = 0
    end_list = []
    for x in range(len(sorted_words)):
        if possible_words_score[x] > highest:
            highest = possible_words_score[x]
    print("AI: Stability = " + str(highest))
    for x in range(len(sorted_words)):
        if possible_words_score[x] == highest:
            end_list.append(possible_words[x])
    return random.choice(end_list)


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


def game(player):
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
    with open("storage/ai", "w+") as x:
        pass
    if not player:
        sys.stdout = open(os.devnull, 'w')
    else:
        sys.stdout = sys.__stdout__
    correct_word = random.choice(file)
    guesses = 0
    inputs = []
    while guesses != 6:
        history = display(inputs, correct_word)
        print("Guess " + str(guesses + 1) + "/6")
        ai_result = ai(sorted_list, score, inputs, history)
        print("AI suggestion: " + ai_result)
        if player:
            inp = input("\n:> ").upper()
            if inp not in sorted_list:
                while 1:
                    inp = input("\n:> ").upper()
                    if inp in sorted_list:
                        break
        else:
            inp = ai_result
        inputs.append(inp)
        if inp == correct_word:
            sys.stdout = sys.__stdout__
            return True, guesses
        guesses += 1
    sys.stdout = sys.__stdout__
    return False, -1


def mainmenu():
    menu = input("Main Menu.\n1. Human\n2. Emulate\n\n>: ")
    while 1:
        if menu.isnumeric() and menu in ["1", "2"]:
            menu = int(menu)
            break
        else:
            menu = input("Main Menu.\n1. Human\n2. Emulate\n\n>: ")
    print("\n\n")
    if menu == 1:
        print("\n\n")
        results.append(game(True))
    if menu == 2:
        emulate = input("How many games would you like to emulate?\n\n>: ")
        while 1:
            if emulate.isdigit() and int(emulate) > 0:
                break
            else:
                emulate = input("How many games would you like to emulate?\n\n>: ")
        print("NOTE: You will not see any game CUI! Please be patient.")
        for x in range(int(emulate)):
            print("Now emulating game " + str(x + 1) + "/" + str(emulate))
            try:
                results.append(game(False))
            except Exception as Exeption:
                print("Exception Raised!" + str(Exeption) + " \\\\ Skipping!")
    won = 0
    lost = 0
    score = 0
    for x in range(len(results)):
        if results[x][0]:
            won += 1
            score += int(results[x][1])
        else:
            lost += 1
    score = float(score / len(results))
    percentage_won = float((won / (won + lost)) * 100)
    print("\n\nWon games: " + str(won) + "\nLost games: " + str(lost) + "\nPercent won: " + str(
        percentage_won) + "\nAverage score: " + str(score))


ALPHABET = ["E", "T", "A", "O", "I", "N", "S", "R", "H", "D", "L", "U", "C", "M", "F", "Y", "W", "G", "P", "B", "V",
            "K", "X", "Q", "J", "Z"]
score = []

results = []

mainmenu()
