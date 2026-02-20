import uuid
import random

class Wallet:
    def __init__(self):
        # Each wallet has a unique public key (UUID) and an initial balance
        self.public_key = str(uuid.uuid4())
        self.private_key = str(uuid.uuid4())  # Simulate private key (store securely in a real app)
        self.balance = random.uniform(0, 1000)  # Simulate an initial balance in USD

    def send_amount(self, receiver, amount):
        # Ensure the sender has enough balance
        if self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
        else:
            raise ValueError("Insufficient funds")
