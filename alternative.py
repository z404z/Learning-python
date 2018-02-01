balance = 42
mpr  = 0.04 #monthlyPaymentRate
air = 0.2 #annualPaymentRate

def calc_debt(balance, mpr, air):
    month = 0
    if month == 0:
        # print('balance:', balance)
        mp = round((balance * mpr), 2) #monthlyPayment = balance * monthlyPaymentRate
        # print('first payment: ', mp)
        balance = ((balance - mp))
        # print('balance - first payment:', balance,)
        balance += round((balance * (air / 12)),2)
        # print('balance in', month,'month', balance)
        # print('___________________________________')
        month += 1

    while month < 12 and month != 12:
        # print('balance before payment: ', balance)
        # print('Now it`s month: ', month)
        mp = round((balance * mpr),2)
        # print('monthly payment: ', mp)
        balance = round((balance - mp), 2)
        # print('balance - payment: ', balance)
        balance += round((balance * (air / 12)), 2)
        # print('balance in', month, 'month', round((balance), 2))
        # print('___________________________________')

        month += 1


    if month == 12:
        return print('Remaining balance: ', round((balance), 2))


calc_debt(balance, mpr, air)