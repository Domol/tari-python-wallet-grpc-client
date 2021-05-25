# Tari gRPC Python Client

Simple implementation of the Tari Protocol wallet gRPC Client.

## Installation
You can install this package using pip:

> pip install git+git://github.com/Domol/tari-python-wallet-grpc-client

You can then use Client class to make calls to Tari wallet RPC.

## Example Usage
Here is a simple code that prints wallet balance:
```python
from tari_python import Client

wallet_address = "localhost:18143"
wallet = Client(wallet_address)

response = wallet.get_balance()
balance = int(response["available_balance"]) / 1e6
print(f"Wallet balance is {balance}")

```


