def makeDictionary(theList):
    dic = {0: 0}
    total = 0
    for i in range(len(theList)):
        key = i 
        if theList[i] != 0:
            dic[key] = theList[i]
        elif theList[i] == 0:
            total = total + 1
    dic[0] = total      
        
    return dic
    
def sparseArraySum(dicOne,dicTwo):
    length = 0
    num = []
    if len(dicOne) < len(dicTwo): 
        length = len(dicTwo)
    elif len(dicTwo) < len(dicOne): 
        length = len(dicOne)
    else:
        length = len(dicOne)
    for i in range(length):
        num.append(0)
    for i in range(length):
        total = dicOne[i] + dicTwo[i]
        num[i] = total
    return num

def main():
    numbersOne = [0,0,0,0,0,4,0,0,0,2,9]
    numbersTwo = [0,0,1,0,0,5,0,0,2,0,3]
    numbers = sparseArraySum(numbersOne,numbersTwo)
    after = makeDictionary(numbers)
    print(after) 
    
main()