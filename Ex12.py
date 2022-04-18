


def calcTax(income):
    totalTax = 0
    if income > 10000 & income <= 20000:
        totalTax = .10 * income

    if income > 20000:
        extraIncome = income - 20000
        totalTax = (.20 * extraIncome) + 1000
    
    print(totalTax)


#testing
calcTax(45000)
