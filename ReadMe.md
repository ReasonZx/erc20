# ERC-20

Token example deployed @ 0x308eF5cC18E4e612343124AE316bc78A4ad4cFdE on Sepolia Testnet

# Deploy

## Testnet
To deploy on a testnet, get your keys for that testnet and the project id from infura.io.

For example Sepolia testnet:
```
$export PUBLIC_KEY="your_public_key"
$export PRIVATE_KEY="your_private_key"
$export WEB3_INFURA_PROJECT_ID="your_infura_project_id"
$brownie networks add Ethereum sepolia host="https://sepolia.infura.io/v3/46213ad1bb2845c5"your_infura_project_id" chainid=11155111
```
```
$brownie run scripts/deployCustomToken.py --network sepolia
```

## Mainnet-fork
To have locally a mainnet-fork go to alchemy.com and create a new app (creates a fork). Then run the following command to add that fork to your local enviroment with brownie:
```
brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.g.alchemy.com/v2/********* accounts=10 mnemonic=******* port=8545
```
Then deploy the SC with:
```
$brownie run scripts/deployCustomToken.py --network mainnet-fork
```
