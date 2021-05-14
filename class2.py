class Bank(object):
    def __init__(self, bank_name, account_name, pin, credit_card):
        self.bank_name = bank_name
        self.account_name = account_name
        self.pin = pin
        self.credit_card = credit_card

    def enter_name(self):
        print('Got the name')

    def enter_pin(self):
        print('Got the pin')

    def enter_credit_card(self):
        print('Got the credit card number')

obj = Bank('HDFC', 'Abyan', '2453', '12345678') 

obj.enter_name()
print(obj.bank_name)

obj.enter_pin()
print(obj.pin)

obj.enter_credit_card()
print(obj.credit_card)