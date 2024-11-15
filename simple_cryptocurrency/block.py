import hashlib
import time

from typing import List, Dict

class Block:
    def __init__(self, index: int, transactions: List[Dict], previous_hash: str, timestamp: float = None):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        block_string = f"{self.index}{self.transactions}{self.previous_hash}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty: int):
        # proof of work algorithm
        required_prefix = '0' * difficulty
        while not self.hash.startswith(required_prefix):
            self.nonce += 1
            self.hash = self.compute_hash()
