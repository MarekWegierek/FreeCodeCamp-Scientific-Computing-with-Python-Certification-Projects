
def arithmetic_arranger(arr, answers = False):
    ''' Returns equations from array in a set, that looks like from primary school '''

    # Input tests section

    if len(arr) > 5:
        return('Error: Too many problems.')
    for eq in arr:
        eqSep = eq.split(' ')
        if (eqSep[1] == '+' or eqSep[1] =='-') == False:
            return("Error: Operator must be '+' or '-'.")
        if (eqSep[0].isdigit() == False) or (eqSep[2].isdigit() == False):
            return("Error: Numbers must only contain digits.")
        if (len(eqSep[0]) > 4) or (len(eqSep[2]) > 4):
            return("Error: Numbers cannot be more than four digits.")
        
    # Meat and potatoes section

    firstLine = ''
    secondLine = ''
    thirdLine = ''
    fourthLine = ''
    for eq in arr:
        eqSep = eq.split(' ')
        biggerNum = max(int(eqSep[0]), int(eqSep[2]))
        wholeLineLength = len(str(biggerNum)) + 2
        spaceBetweenEq = 4*' '
        firstLine = firstLine + (wholeLineLength - len(eqSep[0])) * ' ' + eqSep[0] + spaceBetweenEq
        secondLine = secondLine + eqSep[1] + (wholeLineLength - (len(eqSep[2]) +1)) * ' ' + eqSep[2] + spaceBetweenEq 
        thirdLine = thirdLine + wholeLineLength * '-' + spaceBetweenEq
        if answers == True:
            if eqSep[1] == '+':
                result = int(eqSep[0]) + int(eqSep[2])
                fourthLine = fourthLine + (wholeLineLength - len(str(result)))*' ' + str(result) + spaceBetweenEq
            elif eqSep[1] == '-':
                result = int(eqSep[0]) - int(eqSep[2])
                fourthLine = fourthLine + (wholeLineLength - len(str(result)))*' ' +  str(result) + spaceBetweenEq
    if answers:
        arranged_problems = firstLine.rstrip() + '\n' + secondLine.rstrip() + '\n' + thirdLine.rstrip() + '\n' + fourthLine.rstrip()
    elif not answers:
        arranged_problems = firstLine.rstrip() + '\n' + secondLine.rstrip() + '\n' + thirdLine.rstrip()
    return arranged_problems


