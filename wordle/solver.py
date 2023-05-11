import helpers as stats
import simple as simple
import frequency as frequency

def main():
    real = open("shuffled_real_wordles.txt")
    reals = real.read().split()

    choice = input("\nChoose which algorithm you want to use:\n\n1. Simple(Chooses first word in remaining list)\n2. Letter frequency per position\n3. Common letter strings\n")
    
    match choice:
        case "1":
            starting_word = simple.getSimpleBest()
        case "2":
            starting_word = frequency.getBest()
        case _:
            print("That is not an option, please choose 1")
            return 1

    print("\nWordle\n")
    clone = reals.copy()
    won = False
    attempt = 1
    answer = starting_word
    while attempt <= 6 and won == False:
        print("Please try this word:", answer)
        colors = input("Then enter the colors in format like (BBYGG): ")
        if colors == 'GGGGG':
            won = True
                
        stats.filter(clone, answer, colors)

        match choice:
            case "1":
                answer = simple.simpleAlgorithm(clone)
            case "2":
                answer = frequency.choose(clone)
            case _:
                return 2
        attempt += 1
            
    if won == False:
        print("mb, I failed you")

    real.close()


main()