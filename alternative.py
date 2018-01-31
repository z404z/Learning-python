balance = 42
mpr  = 0.04 #monthlyPaymentRate
air = 0.2 #annualPaymentRate

def calc_debt(balance, mpr, air):
    month = 0
    if month == 0:
        mp = balance * mpr #monthlyPayment = balance * monthlyPaymentRate
        print('first monthly payment: ', mp,'|')
        balance = ((balance - mp))
        print('month 0:', balance)
        month += 1

    while month < 12 and month != 12:

        mp = balance * mpr
        balance = round((balance + ((balance - mp) * (air / 12))), 2)

        month += 1


    if month == 12:
        return round((balance), 2)


print(calc_debt(balance, mpr, air))