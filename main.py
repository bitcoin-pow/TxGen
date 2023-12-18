from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from pprint import pprint
import time
import re

if __name__ == '__main__':

    # rpc_user and rpc_password are set in the bitcoin-pow.conf file
    rpc_user = "USER"
    rpc_pass = "PASS"
    rpc_host = "127.0.0.1"
    btcw_receive_address = "BTCW_RX_ADDRESS_HERE"
    tx_fee   = "0.0001"

    prevHeight = 0
    rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_pass}@{rpc_host}:9332", timeout=1000000)
    while 1:

        commands = [["getblockcount"]]
        height = rpc_connection.batch_(commands)
        if prevHeight != height[0]:
            prevHeight = height[0]
            print(height[0])
            
            txid = 0
            while 1:

                try:
                    txid = rpc_connection.sendtoaddress(btcw_receive_address, tx_fee)    
                    # At some point, we will send and tx will not hit mem pool and we need to abandon tx to get balance back.
                    # keep doing this to keep it simple. It only abandons if it needs to.
                    commands = [["abandontransaction", txid]]                    
                    resp = rpc_connection.batch_(commands)                       
                except Exception as err:
                        # this is good, keep sending txs
                    continue

                print("abandontransaction was successful")    
                break # abandontransaction happened, we are done till next block
                    
                time.sleep(60)
