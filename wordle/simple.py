from helpers import *
   
def simpleAlgorithm(reals):
    return reals[0]

#Returns the word with the lowest round-win average based on a simpleAlgorithm() and 
#filtering out impossible answers based on check() and filter()
def getSimpleBest():
    f = open('output1.txt')
    text = f.read()

    #formatting textfile to store into a dictionary
    text = text.replace(' ', '')
    text = text.replace('\n', '')
    text.strip()

    dlist = text.split(',')

    #store into avg win
    avgwin = {}
    for element in dlist:
        avgwin[element[1:6]] = float(element[8:])


    return min(avgwin, key=avgwin.get)
    #returns 'leant' which is 3.8 round-win average

#Returns a dict that holds all words and their round-win average
#simulates what the best word to start wordle with is based on a simpleAlgorithm and filtering 
def simpleSimulation(reals):
    word_avg_win = {}

    keeptrack = 0
    for starting_word in reals:
        starting_word_win_sum = 0
        if keeptrack % 10 == 0:
            print(starting_word)
        for ending_word in reals:
            clone = reals.copy()
            won = False
            attempt = 1
            answer = starting_word
            while attempt <= 6 and won == False:
                colors = check(answer, ending_word)
                if colors == 'GGGGG':
                    starting_word_win_sum += attempt
                    won = True
                
                filter(clone, answer, colors)
                answer = simpleAlgorithm(clone)
                attempt += 1
            
            if won == False:
                starting_word_win_sum += 6
        
        word_avg_win[starting_word] = starting_word_win_sum / len(reals)
        keeptrack += 1

    return word_avg_win
