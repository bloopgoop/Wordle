def listify(txtfile):
    f = open(txtfile)
    words = []
    for line in f:
        words.append(line[0:5])
    f.close()
    return words

#gets a list of words,a word to compare to, and a color scheme
#deletes all words in the list that the word and color scheme dictate in the rules of Wordle
def filter(rlist, word, colors):
    for i in range(len(word)):
        if colors[i] == 'G':
            list_index = 0
            count = 0
            iterations = len(rlist)
            while count < iterations:
                if rlist[list_index][i] != word[i]:
                    del rlist[list_index]
                else:
                    list_index += 1

                count += 1
        
        elif colors[i] == 'Y':
            list_index = 0
            count = 0
            iterations = len(rlist)
            while count < iterations:
                if word[i] not in rlist[list_index]:
                    del rlist[list_index]
                elif word[i] == rlist[list_index][i]:
                    del rlist[list_index]
                else:
                    list_index += 1
                
                count += 1

        else:
            list_index = 0
            count = 0
            iterations = len(rlist)
            while count < iterations:
                if word[i] in rlist[list_index]:
                    del rlist[list_index]
                else:
                    list_index += 1
                count += 1
#checks two words, and outputs a string or G, Y, or B's
#adds G if same spot and same letter
#adds Y if different spot but has letter
#adds B if does not have letter
def check(starting_word, ending_word):
    colors = ''
    for i in range(len(starting_word)):
        if starting_word[i] == ending_word[i]:
            colors += 'G'
        elif starting_word[i] in ending_word:
            colors += 'Y'
        else:
            colors += 'B'
    return colors

def editString(word, letter, position):
    if position > len(word) - 1:
        print("Error: Index out of range")
        return None
    newString = ''
    iteration = 0
    for char in word:
        if iteration == position:
            newString += letter
        else:
            newString += char
        iteration += 1
    return newString
