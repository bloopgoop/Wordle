#I messed up a calculation in stats.py's simulate_wordle()
#Instead of dividing by amount of words in shuffled_real_wordles.txt,
#I divided by length of ending_word which was 5

#This program is made to correct the mistake by mutiplying all values by 5 and dividing by
#the amount of words in shuffled_real_wordles.txt which is 2315
f = open('flawedoutput1.txt')
text = f.read()

#formatting textfile to store into a dictionary
text = text.replace(' ', '')
text.strip()
text = text.replace('\n', '')

#split by ,
dlist = text.split(',')

#store into avg win
avgwin = {}
for element in dlist:
    avgwin[element[1:6]] = round(((float(element[8:]) * 5) / 2315.0), 2)

w = open('output1.txt', 'w')
w.write(str(avgwin))

w.close()
f.close()
