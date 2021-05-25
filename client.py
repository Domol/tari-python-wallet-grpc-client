import grpc
import wallet_pb2 as wallet
import wallet_pb2_grpc as wallet_grpc
from google.protobuf.json_format import MessageToDict


class Client(object):
    def __init__(self, wallet_address):
        channel = grpc.insecure_channel(wallet_address)
        self.stub = wallet_grpc.WalletStub(channel)

    def get_version(self):
        return MessageToDict(
            self.stub.GetVersion(wallet.GetVersionRequest()),
            preserving_proto_field_name=True,
        )

    def identify(self):
        return MessageToDict(
            self.stub.Identify(wallet.GetIdentityRequest()),
            preserving_proto_field_name=True,
        )

    def transfer(self, address, amount, fee_per_gram, message=""):
        transfer_request = wallet.TransferRequest(
            recipients=[
                wallet.PaymentRecipient(
                    address=address,
                    amount=amount,
                    fee_per_gram=fee_per_gram,
                    message=message,
                )
            ]
        )
        return MessageToDict(
            self.stub.Transfer(transfer_request),
            preserving_proto_field_name=True,
        )

    def transfer_multiple(self, recipients):
        payment_recipients = []
        for recipient in recipients:
            payment_recipients.append(
                wallet.PaymentRecipient(
                    address=recipient["address"],
                    amount=recipient["amount"],
                    fee_per_gram=recipient["fee_per_gram"],
                    message=recipient["message"],
                )
            )
        transfer_request = wallet.TransferRequest(
            recipients=payment_recipients
        )
        return MessageToDict(
            self.stub.Transfer(transfer_request),
            preserving_proto_field_name=True,
        )

    def get_balance(self):
        return MessageToDict(
            self.stub.GetBalance(wallet.GetBalanceRequest()),
            preserving_proto_field_name=True,
        )

    def coin_split(
        self,
        amount_per_split,
        split_count,
        fee_per_gram,
        message,
        lock_height,
    ):
        return MessageToDict(
            self.stub.CoinSplit(
                wallet.CoinSplitRequest(
                    amount_per_split=amount_per_split,
                    split_count=split_count,
                    fee_per_gram=fee_per_gram,
                    message=message,
                    lock_height=lock_height,
                )
            ),
            preserving_proto_field_name=True,
        )

    def get_coinbase(self):
        return MessageToDict(
            self.stub.GetCoinbase(wallet.GetCoinbaseRequest()),
            preserving_proto_field_name=True,
        )

    def get_completed_transactions(self):
        result = self.stub.GetCompletedTransactions(
            wallet.GetCompletedTransactionsRequest()
        )
        while not result.done():
            try:
                yield MessageToDict(
                    result.next(), preserving_proto_field_name=True
                )
            except StopIteration:
                return

    def get_transaction_info(self, transaction_ids):
        return MessageToDict(
            self.stub.GetTransactionInfo(
                wallet.GetTransactionInfoRequest(
                    transaction_ids=transaction_ids
                )
            ),
            preserving_proto_field_name=True,
        )
