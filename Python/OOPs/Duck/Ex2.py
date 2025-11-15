class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement abstract method")

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card 💳")

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal 💻")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI 📱")

# Polymorphism in action
def process_payment(payment_method, amount):
    payment_method.pay(amount)

# Different objects - same method name 'pay'
payments = [CreditCardPayment(), PayPalPayment(), UPIPayment()]

for p in payments:
    process_payment(p, 1000)
