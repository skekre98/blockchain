from blockchain import Blockchain

# Adding a transaction example
blockchain = Blockchain()
blockchain.add_transaction("A", "B", 10)
blockchain.add_transaction("B", "C", 5)

# Once the transactions are ready, they can be added to a new block
new_block = blockchain.add_block()
print("New block mined with hash:", new_block.hash)
