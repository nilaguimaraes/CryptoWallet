from flask import Flask, jsonify, request, abort
from wallet import Wallet
import os

app = Flask(__name__)

# In-memory storage for wallets (in a real-world app, use a database)
wallets = {}

# Route to create a new wallet
@app.route('/api/wallet/create', methods=['POST'])
def create_wallet():
    # Generate a new wallet and return its public key
    wallet = Wallet()
    wallets[wallet.public_key] = wallet
    return jsonify({
        'message': 'Wallet created successfully',
        'public_key': wallet.public_key
    }), 201

# Route to check the balance of a wallet
@app.route('/api/wallet/<public_key>/balance', methods=['GET'])
def check_balance(public_key):
    if public_key not in wallets:
        abort(404, description="Wallet not found")
    
    wallet = wallets[public_key]
    return jsonify({
        'public_key': wallet.public_key,
        'balance': wallet.balance
    })

# Route to send cryptocurrency from one wallet to another
@app.route('/api/wallet/transaction', methods=['POST'])
def send_transaction():
    data = request.get_json()

    sender_key = data.get('sender')
    receiver_key = data.get('receiver')
    amount = data.get('amount')

    if sender_key not in wallets or receiver_key not in wallets:
        abort(404, description="Sender or receiver wallet not found")

    sender = wallets[sender_key]
    receiver = wallets[receiver_key]

    if sender.balance < amount:
        abort(400, description="Insufficient funds")

    # Perform the transaction
    sender.send_amount(receiver, amount)
    
    return jsonify({
        'message': 'Transaction successful',
        'sender_balance': sender.balance,
        'receiver_balance': receiver.balance
    })

# Route to get current cryptocurrency prices (simulated)
@app.route('/api/crypto/price', methods=['GET'])
def get_crypto_price():
    # Simulate current price (In a real app, call an external API like CoinGecko)
    prices = {
        'bitcoin': 35000,  # USD
        'ethereum': 2400   # USD
    }
    return jsonify(prices)

# Error handler for not found
@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({'error': 'Not found', 'message': error.description}), 404

# Error handler for bad requests
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request', 'message': error.description}), 400

if __name__ == '__main__':
    app.run(debug=True)
