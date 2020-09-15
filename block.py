# Transactions are packed into blocks. 
# A block can contain one or many transactions. 
from hashlib import sha256
# Using Secure Hash Algorithm 2 to hash the blocks 
import json 
class Block: 
    def __init__(self, index, transactions, timestamp):
        # index is a unique ID for 
        self.index = index 
        self.transactions = transactions
        self.timestamp = timestamp

    def compute_hash(block):

        # Compute the hash of the string
        # This is done by converting the object into json

        block_string = json.dumps(self/__dict__. sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
        