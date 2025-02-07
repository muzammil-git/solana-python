from fastapi import APIRouter
import solana
from solana.rpc.api import Client
from solana.rpc.api import Pubkey

from solders.keypair import Keypair # type: ignore
from solders.message import MessageV0 # type: ignore
from solders.system_program import TransferParams, transfer
from solders.transaction import VersionedTransaction, Transaction # type: ignore
from solders.message import Message # type: ignore
from solana.rpc.core import RPCException
    

router1 = APIRouter()


def connectNetwork():
    '''
    Connect to the Network
    '''
    # Connect to Solana Devnet
    solana_client = Client("https://api.devnet.solana.com")

    # Check if the connection is successful
    response = solana_client.is_connected()
    print(f"✅ Connected: {response}")
    
    blockhash = solana_client.get_latest_blockhash()
    # print("Latest Blockhash:", blockhash.value.blockhash)
    
    return solana_client
    
# print(connectNetwork())


def readBalancefromSolnet():
    '''
    Read Balance from Solana Network
    '''
    # Constants
    LAMPORTS_PER_SOL = 1_000_000_000  # 1 SOL = 1 billion lamports
    SOLANA_DEVNET_RPC_URL = "https://api.devnet.solana.com"

    # Connect to the Solana Devnet
    solana_client = Client(SOLANA_DEVNET_RPC_URL)

    # Address to check balance for
    wallet_address = Pubkey.from_string("CenYq6bDRB7p73EjsPEpiYN7uveyPUTdXkDkgUduboaN")

    # Get balance (returns in lamports)
    balance_response = solana_client.get_balance(wallet_address)
    balance_lamports = balance_response.value

    # Convert to SOL
    balance_sol = balance_lamports / LAMPORTS_PER_SOL

    # Print results
    print(f"The balance of the account at {wallet_address} is {balance_sol} SOL")
    print("✅ Finished!")

# readBalancefromSolnet()


def test():
    '''
    Read Balance from Solana Network
    '''
    # Constants
    LAMPORTS_PER_SOL = 1_000_000_000  # 1 SOL = 1 billion lamports
    public_key = "CenYq6bDRB7p73EjsPEpiYN7uveyPUTdXkDkgUduboaN"

    solana_client = connectNetwork()
    
    # Address to check balance for
    wallet_address = Pubkey.from_string(public_key)

    # Get balance (returns in lamports)
    balance_response = solana_client.get_balance(wallet_address)
    balance_lamports = balance_response.value

    # Convert to SOL
    balance_sol = balance_lamports / LAMPORTS_PER_SOL
    
    account_info =  solana_client.get_account_info(pubkey=wallet_address)
    # print(account_info)
    
    is_executable = account_info.value.executable
    print("Is executable: ", is_executable)
    
    
    try:
        # Load from disk
        sender = Keypair()  # let's pretend this account actually has SOL to send
        receiver = Keypair()
        
        ixns = [transfer(TransferParams(
                from_pubkey=sender.pubkey(), 
                to_pubkey=receiver.pubkey(), 
                lamports=1_000_000
            )
        )]
        
        msg = Message(ixns, sender.pubkey())
        
        tx = Transaction(
            from_keypairs= [sender],
            message= msg,
            recent_blockhash= solana_client.get_latest_blockhash().value.blockhash,
        )
        
        response = solana_client.send_transaction(tx)
        print("Transaction Signature:", response.value)
    
    except RPCException as e:
        print('Error: ', e)   
    
    except Exception as e:
        print("Error sending transaction: ", e)
    
    
    # Print results
    print("-----------------------------------")
    print(f"The balance of the account at {wallet_address} is {balance_sol} SOL")
    print("✅ Finished!")
    
    
test()


