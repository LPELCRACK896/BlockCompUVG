
from fastapi import APIRouter

from components.fastapi.routes.blockchain.wallets import wallets_router


block_chain_router = APIRouter()


block_chain_router.include_router(wallets_router, prefix="/wallets")
