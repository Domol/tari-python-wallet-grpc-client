from client import Client

wallet_address = "localhost:18143"
wallet = Client(wallet_address)
result = wallet.get_balance()
if "available_balance" in result:
    balance_utari = int(result["available_balance"])
    print(f"Wallet balance is: {balance_utari / 1e6}")
if "pending_incoming_balance" in result:
    pending_incoming = int(result["pending_incoming_balance"])
    print(f"Wallet pending incoming balance is: {pending_incoming / 1e6}")
