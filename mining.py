import time
import json
import hashlib
import requests


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

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

    def get_balance(self):
        balance = requests.get(
            'https://lambda-treasure-hunt.herokuapp.com/api/bc/get_balance/',
            headers={
                "Authorization":
                "Token 09c8d609debf1f798768afe66b8039f37fec5e67"
            })
        if balance.json()["errors"] is None:
            return balance.json()["messages"]
        else:
            print("Error", balance.json()["errors"])


# Todo: Get new proof

lambda_coin = Blockchain()

if __name__ == '__main__':
    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server and look for a new one
        request = requests.get(
            'https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/',
            headers={
                "Authorization":
                "Token 09c8d609debf1f798768afe66b8039f37fec5e67"
            })
        last_proof = request.json()['proof']
        difficulty = request.json()['difficulty']
        print(f"last proof is {last_proof}")
        proof = 0
        while lambda_coin.valid_proof(last_proof, proof, difficulty) is False:
            proof += 1
            # TODO: When found, POST it to the server {"proof": new_proof}
            # TODO: If the server responds with 'New Block Forged'
            response = requests.post(
                'https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/',
                headers={
                    "Authorization":
                    "Token 09c8d609debf1f798768afe66b8039f37fec5e67"
                },
                json={'proof': proof})
            print(response.json())
            if response.json()['errors'] is None:
                coins_mined += 1
                print('Created the proof')
            # add 1 to the number of coins mined and print it.  Otherwise,
            # print the message from the server.
            else:
                print(response.json()['errors'])
