#!/usr/bin/python3

from brownie import Token, accounts, network 
import os 




def main():
    # got this bit from Patrick Collins tutorial on YT: https://www.youtube.com/watch?v=QfFO22lwSw4 around 6:30 in to the video
    dev = accounts.add(os.getenv('PRIVATE_KEY'))

    return Token.deploy("Test Token", "TST", 18, 1e21, {'from': dev})
