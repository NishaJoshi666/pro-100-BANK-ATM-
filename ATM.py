class atm(object):
    def __init__(self,usersATMCardNumber,pinNumber):
        self.usersATMCardNumber = usersATMCardNumber
        self.pinNumber = pinNumber

    def start(self):
        print('started')

    def end(self):
        print('ended')

CashWithdrawl = atm('CashWithdrawl-Users ATM Card Number : 234543','CashWithdrawl-Pin Number : 335523')
BalanceEnquiry = atm('BalanceEnpuiry-Users ATM Card Number : 453525','BalanceEnpuiry-Pin Number : 334001')
print(CashWithdrawl.pinNumber)
print(CashWithdrawl.usersATMCardNumber)
print(BalanceEnquiry.usersATMCardNumber)
print(BalanceEnquiry.pinNumber)