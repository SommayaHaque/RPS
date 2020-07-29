def main():
    initials()
    dateprinter()
    print()
    a= input('Enter a statement to count vowels/constanants: ')
    count_vowels(a)
    count_cons(a)

#Initial Finder
def initials():
    name=input('Enter a name: ')
    s=name.split()
    e=' '
    for word in s:
        e+=word[0]+'.'
    print('Initials: '+e)

#Date Printer 
def dateprinter():
    months=[' ','January','February','March','April','May','June','July','August','September','October','November','December']
    date=str(input('Enter date in mm/dd/yyyy format: '))
    d=date.split('/')
    month_id=int(d[0])
    d[0]=months[month_id]
    e=' '
    for word in d:
        print(word,end=' ')

#Vowel Counter 
def count_vowels(word):
    vowels= 'aeiou'
    countV=0
    for ch in word:
        if vowels.find(ch)>=0:
            countV=countV+1
    print('Number of vowels:',countV)
    
    return countV

#Constanant Counter
def count_cons(word):
    vowels= 'aeiou'
    countC=0
    for ch in word:
        if vowels.find(ch)<=0:
            countC=countC+1
    print('Number of constanats:',countC)
    return countC

main()
