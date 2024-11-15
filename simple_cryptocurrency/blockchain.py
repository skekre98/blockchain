from block import Block

class Blockchain:
    def __init__(self, difficulty: int = 2):
        self.chain = []
        self.transactions = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_transaction(self, sender, recipient, amount):
        transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
        self.transactions.append(transaction)

    def add_block(self):
        if not self.transactions:
            return None  # No transactions to add

        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), self.transactions, previous_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.transactions = []  # Clear the transactions once added to the block
        return new_block
