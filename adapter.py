"""
 The Adapter pattern allows incompatible interfaces to work together by wrapping an existing class with a new interface.
"""

class BankService:
    def make_payment(self, amount):
        print(f"Paying ${amount} via BankService")


class PaymentServiceInterface:
    def pay(self, amount):
        pass

"""
- This adapts BankService to a new interface: pay(), which is expected by the client.
- It acts as a wrapper, internally translating pay(amount) into make_payment(amount).
"""
# added later to support the pay method
class BankServiceAdapter(PaymentServiceInterface):
    def __init__(self, bank_service: BankService):
        self.bank_service = bank_service

    def pay(self, amount):
        self.bank_service.make_payment(amount)


def process_payment(payment_service: PaymentServiceInterface, amount):
    payment_service.pay(amount)


bank_service_adapter = BankServiceAdapter(BankService())

process_payment(bank_service_adapter, 100)