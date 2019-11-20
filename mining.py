import time
import json
import hashlib
import requests


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
    def valid_proof(last_proof, proof, difficulty):
        """
        Validates the Proof:  Does hash(last_proof, proof) contain 4
        leading zeroes?
        """
        # encode a guess
        guess = f"{last_proof}{proof}".encode()
        # hashing the guess
        guess_hash = hashlib.sha256(guess).hexdigest()
        # return True if the last 4 digits of the hash ar zreos
        return guess_hash[:6] == "0" * difficulty


# Todo: Get new proof

lambda_coin = Blockchain()

response = lambda_coin.get_proof()
# print(response)
response.update({"timestamp": time()})
difficulty = response.get('difficulty')
last_proof = response.get('proof')
last_block = response
last_block_string = json.dumps(last_block, sort_keys=True).encode()

# proof = lambda_coin.valid_proof(47616702, 1, 6)
# print(proof)


def proof_work(last_proof=47616702, new_proof=1, n=6):
    """
        takes in the last proof and new proof, level of difficulty - n
        if hash(last_proof, new_proof) begins with n leading zero
        return proof
        """
    if lambda_coin.valid_proof(last_proof, new_proof, n):
        return (new_proof)
    else:
        ne


print(proof_work())
