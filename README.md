# token-mix

A bare-bones implementation of the Ethereum [ERC-20 standard](https://eips.ethereum.org/EIPS/eip-20), written in [Solidity](https://github.com/ethereum/solidity).


## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html), if you haven't already.

2. Download the mix.

    ```bash
    brownie bake token
    ```

3. Create a .env file ( replace it with your project id and private key). Alternatively, you can just type these command in a terminal and not create a .env file. 
```
        export WEB3_INFURA_PROJECT_ID='112233fdfdfdfdfdf'
        export PRIVATE_KEY='0x3434343434343434343434343434'
```


- Sign up for Infura here: https://infura.io/
- Export your private key from metamask this way https://metamask.zendesk.com/hc/en-us/articles/360015289632-How-to-Export-an-Account-Private-Key



4. Edit the scripts/token.py script to fetch the private key from the env variables. I also add the `import os` line to the file.
```
#!/usr/bin/python3

from brownie import Token, accounts, network 
import os 

def main():
    
    dev = accounts.add(os.getenv('PRIVATE_KEY'))

    return Token.deploy("Test Token", "TST", 18, 1e21, {'from': dev})
```



5) If you don't have testnet ETH: Get Testnet Ether on either Rinkeby or Kovan network and load up your eth wallet. 
https://support.mycrypto.com/how-to/getting-started/where-to-get-testnet-ether


6) Deploy to Rinkeby / kovan testnet
 ```
brownie run scripts/token.py --network kovan  
```



## License

This project is licensed under the [MIT license](LICENSE).
