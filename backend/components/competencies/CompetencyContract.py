from typing import AnyStr
import json
class CompetencyContract:
    path: AnyStr
    abi: dict
    address: AnyStr

    def __init__(self, path: AnyStr = './projects/truffle-compiler/build/contracts/CompetencySystem.json'):
        self.path = path
        self.__load_contract()




    def __load_contract(self):
        with open(self.path) as f:
            contract_json = json.load(f)
            self.abi = contract_json['abi']
            networks = contract_json['networks']
            network_id = "1337"
            self.address = networks[network_id]['address']


if __name__ == "__main__":

    comp = CompetencyContract()



