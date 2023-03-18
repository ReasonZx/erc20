from brownie import customToken, config, network
from scripts import helpfulScripts
from web3 import Web3


def deployCustomToken():
    account = helpfulScripts.getAccount()
    
    customTokenSC = customToken.deploy(
        Web3.toWei(1000,"ether"),
        {'from': account},
    )
    return customTokenSC


def main():
    deployCustomToken()