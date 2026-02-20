# Crypto Wallet API

This is a simple Flask-based API for managing cryptocurrency wallets.

## Features:
- Create a new wallet
- Check wallet balance
- Send cryptocurrency from one wallet to another
- Get current cryptocurrency prices (simulated)

## Setup

1. Install Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the application:

    ```bash
    python app.py
    ```

3. Access the API at `http://127.0.0.1:5000`.

## API Endpoints

### Create a new wallet
- **URL**: `/api/wallet/create`
- **Method**: `POST`
- **Response**:
    ```json
    {
        "message": "Wallet created successfully",
        "public_key": "public_key_value"
    }
    ```

### Check wallet balance
- **URL**: `/api/wallet/{public_key}/balance`
- **Method**: `GET`
- **Response**:
    ```json
    {
        "public_key": "public_key_value",
        "balance": 100.50
    }
    ```

### Send cryptocurrency
- **URL**: `/api/wallet/transaction`
- **Method**: `POST`
- **Request**:
    ```json
    {
        "sender": "sender_public_key",
        "receiver": "receiver_public_key",
        "amount": 50.00
    }
    ```
- **Response**:
    ```json
    {
        "message": "Transaction successful",
        "sender_balance": 50.50,
        "receiver_balance": 200.00
    }
    ```

### Get current cryptocurrency prices
- **URL**: `/api/crypto/price`
- **Method**: `GET`
- **Response**:
    ```json
    {
        "bitcoin": 35000,
        "ethereum": 2400
    }
    ```

## License
MIT License
