
class Category:

    def __init__(self,name):
        self.name = name
        self.ledger = []
    
    def __str__(self):
        title = f'{self.name:*^30}\n'
        entries = ''
        total = 0
        for elem in self.ledger:
            entries += f'{elem["description"][:23]:23}' + f'{elem["amount"]:>7.2f}' + '\n'
            total += float(elem["amount"])
        
        return title + entries + f'Total: {total}'
    
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if (self.check_funds(amount=amount)):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
            
    def get_balance(self):
        total = 0
        for elem in self.ledger:
            total = total + elem["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount=amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False
    
    def check_funds(self, amount):
        if(self.get_balance()) >= amount:
            return True
        return False
        
def create_spend_chart(list):

    # Processing data before chart creation
    negative_balance = 0
    list_of_negative_balances = []
    percentage_of_balances = []
    
    for elem in list:
        """ print(elem.ledger, len(elem.ledger)) """
        if len(elem.ledger) > 1:
            for transaction in elem.ledger:
                if transaction["amount"] <= 0:
                    negative_balance += transaction["amount"]
                    list_of_negative_balances.append(transaction["amount"])
        elif len(elem.ledger) == 1:
            list_of_negative_balances.append(0)
            
    for elem in list_of_negative_balances:
        percentage_of_balances.append(round(((100*elem)/negative_balance)/10))
    
    # Making a chart
    listOfTitles = []                   
    lenOfTitles = []
    for instance in list:
        listOfTitles.append(instance.name)
        lenOfTitles.append(len(instance.name))
    longestWordLen = max(lenOfTitles)

    result = []
    result2 = ''
    dashedLine = 4*' ' + 3*len(list)* '-' + '-'

    titles = []
    titlesListFormatted = []
    titlesListFormatted2 = ''
    
    # Making a chart above dashed lines
    for i in range(0,101,10):
        str_for_o = ''
        for elem in percentage_of_balances:
            if elem*10 >= i:
                str_for_o += ' ' + 'o' + ' '
            else:
                str_for_o += 3*' '
        result.append(str((3 - len(str(i)))*' ' + str(i) + '|' + str_for_o +'\n'))
    result.reverse()
    for elem in result:
        result2 += str(elem)
    
    # Making a list of titles to display below dashedLine
    for elem in listOfTitles:
        if len(elem) < longestWordLen:
            titles.append(f'{elem:{longestWordLen}}')
        else:
            titles.append(f'{elem}')

    for i in range(0, longestWordLen):
        tempList = ''
        for j in range(0, len(list)):
            tempList += f'{titles[j][i]}'
        titlesListFormatted.append(f'{tempList}')
    
    for elem in titlesListFormatted:
        titlesString = ''
        for i in range(0, len(listOfTitles)):
            titlesString += elem[i] + 2*' '
        titlesListFormatted2 += 5*' ' + f'{titlesString:25}' + '\n' 

    return 'Percentage spent by category' + '\n' + result2 + dashedLine + '\n' + str(titlesListFormatted2) + '\n' 
