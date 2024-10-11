from web3 import Web3
from typing import AnyStr


def vitals_connection(conn: Web3):
    return conn.is_connected()


def create_wallet(conn: Web3):
    account = conn.eth.account.create()

    address = account.address
    private_key = account.key.hex()

    return {
        "address": address,
        "private_key": private_key
    }

class CWeb3:
    url: AnyStr

    def __init__(self, url):
        self.url = url

    def get_connection(self):
        return Web3(Web3.HTTPProvider(self.url))
