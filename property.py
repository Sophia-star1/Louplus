class Account(object):
    def __init__(self):
        self.__amt=0
        self.rate=rate

    @property
    def amount(self):
        return self.__amt

    @property
    def cny(self):
        return self.__amt*self.rate

    @amount.setter
    def amount(self,value):
        if value<0:
            print("Sorry,no negative amount in the account,")
            return
        self.__amt=value

if__name__='__main__':
    acc=Account(rate=6.6)
    acc.amount=20
    print("Dollars amount:",acc.amount)
    print("In CNY:",acc.cny)
    acc.amount=-100
    print("Dollars amount:",acc.amount)
