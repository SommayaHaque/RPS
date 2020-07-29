#Score Calc By Sommaya Haque

SCORES= [] #empty set that will have scores added to it

def calc():
    SN = int(input('Enter number of test scores: '))

    getscores(SN)
    print("The average score is", "{:.2f}".format(gettotal(SCORES)/(SN)))
    SCORES.remove(min(SCORES)) #removes smallest score
    gettotal(SCORES) #finds total of the scores
    
    print("The average with the lowest score dropped is", "{:.2f}".format(gettotal(SCORES)/(SN-1)))
    #Divides the score total by 5 for the average
    
def getscores(scoreNum): #this function prompts the user to input scores
    print('Please enter your', scoreNum, 'test scores')
    for i in range(int(scoreNum)): #for loop, asks for scores scoreNum times
        r=float(input('Enter a test score: '))
        SCORES.append(r) #adds the score to the list SCORES
    return r

def gettotal(L): #calculates the total by adding all elements in SCORES
    total=sum(L)
    return(total)

calc() #calls calc
