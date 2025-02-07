from fastapi import APIRouter
from solana.rpc.api import Pubkey
from solana.rpc.api import Client
import requests


# a = requests.get("https://google.com")
# print(a)
# Solana Explorer
# https://explorer.solana.com/address/CenYq6bDRB7p73EjsPEpiYN7uveyPUTdXkDkgUduboaN?cluster=devnet

router2 = APIRouter()


PUBLIC_KEY = "HWCbt7iyp9PSfUhQmkE8CoVvgHY5kMZ4MxfqNdw1xKFz"

def readBalance(public_key : str):
    '''
    The script loads the public key, connects to DevNet, and checks the balance
    '''
    LAMPORTSPERSOL=1_000_000_000 # 1 SOL = 1 billion lamports
    
    connection = Client('https://api.devnet.solana.com')
    
    try:
        publickey = Pubkey.from_string(public_key)
        
        balanceResponse = connection.get_balance(publickey)
        balanceInLamports = balanceResponse.value
        print("Balance In Lamports: ", balanceInLamports)
        
        balanceInSol = balanceInLamports/LAMPORTSPERSOL
        print("Balance In SOl: ", balanceInSol)
    except Exception as e:
        print("Error: ", e)
        
        
    
# readBalance(public_key=PUBLIC_KEY)
# readBalance(public_key="CenYq6bDRB7p73EjsPEpiYN7uveyPUTdXkDkgUduboaN")
