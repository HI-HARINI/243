from web3 import Web3
from web3.middleware import geth_poa_middleware

url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(API_url))

Block_data = web3.eth.get_block('latest')
print('Block Data:',Block_data)

print('gasUsed:',Block_data ['gasUsed'])
block_transaction_count = web3.eth.get_block_transaction_count(4387523)
print(block_transaction_count)
transaction_fee = web3.eth.fee_history(876,"latest",None)
print(transaction_fee)

print('transaction data:',Block_data ['transactions'])
transaction = web3.eth.get_transaction('0x4e24a8bb601dea23e7d4e90766ac824d2a16c4984734455b91c3c826ba447193')
print('data',transaction)