from projects.fastapi.config.config import mongo_db, block_chain_network
from components.services.CWeb3 import CWeb3, create_wallet
from fastapi import  APIRouter
from web3 import Web3

wallets_router = APIRouter()
GANACHE_URL = block_chain_network.URL


#@wallets_router.get("/")
async def get_wallets():
    web3_instance = CWeb3(url=GANACHE_URL)
    web3_conn: Web3 = web3_instance.get_connection()

    wallets = web3_conn.eth.accounts

    return {"wallets": wallets}