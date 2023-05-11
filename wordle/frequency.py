"""
Pick a word from list based on which letter occurs the most
then which position that letter occurs the most
"""
from helpers import *

def choose(words):
    clone = words.copy()
    print(len(clone))
    bufferWord = "XXXXX"
    bufferColor = "BBBBB"

    exceptions = []

    iteration = 0
    while iteration < 5 and len(clone) > 1:
        #Find the most common letter in the list first
        letter_dict = count_letters(clone)
        mostCommonLetter = findMostCommonLetter(letter_dict, exceptions)
        exceptions.append(mostCommonLetter)

        #Then find which position this letter occurs the most
        mostCommonSpace = findMostCommonSpace(clone, mostCommonLetter)

        #Update bufferWord and bufferColor
        bufferWord = editString(bufferWord, mostCommonLetter, mostCommonSpace)
        bufferColor = editString(bufferColor, 'G', mostCommonSpace)
        
        filter(clone, bufferWord, bufferColor)
        
        iteration += 1

    return clone[0]

#counts overall how many times each letter was used and returns it
def count_letters(list):
    letter_count = {}
    for word in list:
        for char in word:
            if char not in letter_count:
                letter_count[char] = 1
            else:
                letter_count[char] += 1
    return letter_count

#counts the amount of times a letter was used in each position
#returns a list of dictionaries, list index refers to specific position of letter in word
def count_letters_per_space(list):
    space = []
    first = {}
    second = {}
    third = {}
    fourth = {}
    fifth = {}
    for word in list:
        if word[0] not in first:
            first[word[0]] = 1
        else:
            first[word[0]] += 1
        
        if word[1] not in second:
            second[word[1]] = 1
        else:
            second[word[1]] += 1
        
        if word[2] not in third:
            third[word[2]] = 1
        else:
            third[word[2]] += 1

        if word[3] not in fourth:
            fourth[word[3]] = 1
        else:
            fourth[word[3]] += 1
        
        if word[4] not in fifth:
            fifth[word[4]] = 1
        else:
            fifth[word[4]] += 1

    space.append(first)
    space.append(second)
    space.append(third)
    space.append(fourth)
    space.append(fifth)

    return space             
        
def findMostCommonSpace(words, letter):
    posCount = count_letters_per_space(words)
    mostCommonSpace = -1
    most = 0
    for i in range(5):
        if letter in posCount[i]:
            if posCount[i][letter] > most:
                mostCommonSpace = i
                most = posCount[i][letter]
    return mostCommonSpace

def findMostCommonLetter(count_of_letters, exceptions):
    clone = count_of_letters.copy()
    for exception in exceptions:
        if len(clone) == 1:
            return list(clone.keys())[0]
        del clone[exception]
    return max(clone, key=clone.get)

#unused
def probLetterInSpot(words):
    overall = count_letters(words)
    posCount = count_letters_per_space(words)
    position = []

    #pack array
    for i in range(5):
        position.append(getProbability(posCount[i], overall))
    #search for highest probability
    highest_index = -1
    highest_key = ''
    highest_value = 0
    for i in range(5):
        if position[i][max(position[i], key=position[i].get)] > highest_value:
            highest_index = i
            highest_key = max(position[i], key=position[i].get)
            highest_value = position[highest_index][highest_key]
    
    print("at position[", highest_index, "], the highest key-value pair is", highest_key, ":", highest_value)

#returns a dict of probabilities of letters being in that specific spot
#unused
def getProbability(posDict, overallDict):
    posProbability = {}
    for key in posDict:
        posProbability[key] = posDict[key] / overallDict[key]
    return posProbability
        
def simulateFrequency(words):
    word_avg_win = {}

    keeptrack = 0
    for starting_word in words:
        starting_word_win_sum = 0
        if keeptrack % 10 == 0:
            print(round(((keeptrack / len(words)) * 100), 2), '%')
        for ending_word in words:
            clone = words.copy()
            won = False
            attempt = 1
            answer = starting_word
            while attempt <= 6 and won == False:
                colors = check(answer, ending_word)
                if colors == 'GGGGG':
                    starting_word_win_sum += attempt
                    won = True
                
                filter(clone, answer, colors)
                answer = choose(clone)
                attempt += 1
            
            if won == False:
                starting_word_win_sum += 6
        
        word_avg_win[starting_word] = starting_word_win_sum / len(words)
        keeptrack += 1

    return word_avg_win

def getBest():
    return "leant"