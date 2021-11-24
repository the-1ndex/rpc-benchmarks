from locust import HttpUser, task, tag
import random

pubkeys = [pubkey.strip() for pubkey in open('pubkeys.txt').readlines()]
serum_accounts = [pubkey.strip() for pubkey in open('serum_accounts.txt').readlines()]


class APIUser(HttpUser):
    @tag('gma')
    @task
    def get_confirmed_transaction(self):
        random_pubkeys = random.choices(pubkeys, k=100)
        data = {"jsonrpc": "2.0",
                "id": 1,
                "method": "getMultipleAccounts",
                "params": [random_pubkeys, {
                    "encoding": "base64",
                    "commitment": "recent"
                }]}
        self.client.post('', json=data)

    @tag('gpa')
    @task
    def get_serum_accounts(self):
        pubkey = random.choice(serum_accounts)
        data = {
            "method": "getProgramAccounts",
            "jsonrpc": "2.0",
            "params": [
                "9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin",
                {
                    "encoding": "base64",
                    "commitment": "recent",
                    "filters": [
                        {
                            "memcmp": {
                                "offset": 45,
                                "bytes": pubkey
                            }
                        },
                        {
                            "dataSize": 3228
                        }
                    ]
                }
            ],
            "id": "1"
        }
        self.client.post('', json=data)
