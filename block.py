from hashlib import sha256
import json

class Block:
    
    def __init__(self, index, transactions, timestamp, previous_hash):
        """
        Constructor for the `Block` class.
        :param index: Unique ID of the block.
        :param transactions: List of transactions.
        :param timestamp: Time of generation of the block.
        """
        self.index = index 
        self.transactions = transactions 
        self.timestamp = timestamp

    

    def compute_hash(block):
   
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()



# Now the class for the Blockchain which is a chain of the blocks

class Blockchain:
    def __init__(self): 
       self.unconfirmed_transactions = [] # not mined yet
       self.chain = []
       self.create_genesis_block()

    difficulty = 2
   

    

    def proof_of_work(self, block):
        
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

    
    def add_block(self, block, proof):
       
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not Blockchain.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)
    

    def mine (self): 

# if its empty
        if not self.unconfirmed_transactions: 
            return False
        
        last_block = self.last_block

        new_block = Block(index = last_block.index + 1,
                          transactions = self.unconfirmed_transactions,
                          timestamp = time.time(),
                          previous_hash = last_block.hash)
        
        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index