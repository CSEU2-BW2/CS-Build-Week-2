import time
import json
import hashlib
from time import time
from uuid import uuid4
import requests

import sys


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)

        return block

    @staticmethod
    def hash(self, block):
        """
        Creates a SHA-256 hash of a Block
        :param block": <dict> Block
        "return": <str>
        """

        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        return hex_hash

    def get_proof(self):
        response = requests.get(
            'https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/',
            headers={
                "Authorization":
                "Token 09c8d609debf1f798768afe66b8039f37fec5e67"
            })
        response_json = response.json()
        return response_json

    @staticmethod
    def hash(block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

    @staticmethod
    def valid_proof(last_proof, new_proof, difficulty=int()):
        """
        Validates the Proof: Does hash(last_proof, new_proof) 
        contain N leading zeroes, where N is the current difficulty level?
        :param last_proof: 
        :param new_proof: <int?> The value that when combined with the
        stringified previous block results in a hash that has the
        correct number of leading zeroes.
        :return: True if the resulting hash is a valid proof, False otherwise
        """
        guess = f'{last_proof}{new_proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:difficulty] == "0" * difficulty

   


# Todo: Get new proof

lambda_coin = Blockchain()

response = lambda_coin.get_proof()
print(response)
response.update({"timestamp": time()})
difficulty = response.get('difficulty')
last_proof = response.get('proof')
last_block = response
last_block_string = json.dumps(last_block, sort_keys=True).encode()



